import csv

from DataStructures.conditions_state import ConditionsState
from DataStructures.data_point import DataPoint
from DataStructures.plot import Plot
from DataStructures.vi_state import VIState
from Helpers.utility import get_plot_missing_dates, convert_str_to_int_date


class Interpolator:
    def fill_missing_data(self, plots: list[Plot]) -> None:
        """
        Fill in the missing data points for each plot in given list of plots
        :param plots: list[Plot] - List of plots with data point lists to fill missing data for
        :return: None
        """
        for plot in plots:
            missing = get_plot_missing_dates(plot)
            new_data_points = self.generate_data_points(missing, plot, plots)
            for dp in new_data_points:
                self.insert_data_point(dp, plot)

    def generate_data_points(self, dates: list[int], plot: Plot, plots: list[Plot]) -> list:
        """
        For a given plot, generate a list of data points that fill the missing data in the plot
        :param dates: list[int] - List of missing dates in the plot given
        :param plot: Plot - The plot to generate missing data points for
        :param plots: list[Plot] - The list of plots that 'plot' is in. (Used to find values for interpolating between)
        :return: list[DataPoints] - A list of data points
        """
        new_data_points = []
        for date in dates:
            lerped_cigreen0: float = self.lerp_fill(date, dates, plot.data_points, "cigreen0")
            lerped_cigreen: float = self.lerp_fill(date, dates, plot.data_points, "cigreen")
            lerped_evi2: float = self.lerp_fill(date, dates, plot.data_points, "evi2")
            lerped_gndvi0: float = self.lerp_fill(date, dates, plot.data_points, "gndvi0")
            lerped_gndvi: float = self.lerp_fill(date, dates, plot.data_points, "gndvi")
            lerped_ndvi: float = self.lerp_fill(date, dates, plot.data_points, "ndvi")
            lerped_rdvi: float = self.lerp_fill(date, dates, plot.data_points, "rdvi")
            lerped_savi: float = self.lerp_fill(date, dates, plot.data_points, "savi")
            lerped_sr: float = self.lerp_fill(date, dates, plot.data_points, "sr")
            new_vi_state: VIState = VIState(lerped_cigreen0, lerped_cigreen, lerped_evi2, lerped_gndvi0,
                                            lerped_gndvi, lerped_ndvi, lerped_rdvi, lerped_savi, lerped_sr)
            air_temp: float = self.other_data_point_fill(date, dates, plot.data_points, "air_temp", plots)
            dewpoint: float = self.other_data_point_fill(date, dates, plot.data_points, "dewpoint", plots)
            relative_humidity: float = self.other_data_point_fill(date, dates, plot.data_points,
                                                                  "relative_humidity", plots)
            soil_temp_2in: float = self.other_data_point_fill(date, dates, plot.data_points, "soil_temp_2in", plots)
            soil_temp_8in: float = self.other_data_point_fill(date, dates, plot.data_points, "soil_temp_8in", plots)
            precipitation: float = self.other_data_point_fill(date, dates, plot.data_points, "precipitation", plots)
            solar_radiation: float = self.other_data_point_fill(date, dates, plot.data_points, "solar_radiation", plots)
            new_conditions_state = ConditionsState(air_temp, dewpoint, relative_humidity, soil_temp_2in,
                                                   soil_temp_8in, precipitation, solar_radiation)
            new_dp = DataPoint(date, plot.data_points[0].season_type, "Interpolated", plot.variety_index,
                               plot.replication_variety, new_vi_state, new_conditions_state)
            new_data_points.append(new_dp)
        return new_data_points

    @staticmethod
    def lerp_fill(date: int, dates: list[int], data_points: list, goal_val: str) -> float:
        """
        Linearly interpolate between the closest known dates
        :param goal_val: str - The value type name to interpolate for
        :param date: int - The date that needs an interpolated value
        :param dates: list[int] - The full list of known dates for the plot
        :param data_points: list[DataPoints] - Datapoints to reference values from
        :return: float - interpolated value for given date
        """

        def find_left_index():
            current_i = dates.index(date)
            # Iterate over the previous dates in reverse order
            for i in range(current_i, 0, -1):
                if abs(dates[i - 1] - dates[i]) > 1:
                    # Found a gap of more than 1 day
                    return dates[i] - 1
            return dates[0] - 1

        def find_right_index():
            current_i = dates.index(date)
            # Iterate over the previous dates
            for i in range(current_i, len(dates) - 1):
                if dates[i + 1] - dates[i] > 1:
                    # Found a gap of more than 1 day
                    return dates[i] + 1

            return dates[len(dates) - 1] + 1

        def find_val(index):
            for dp in data_points:
                value = getattr(dp.conditions_state, goal_val, None)
                if value is None:
                    value = getattr(dp.vi_state, goal_val, None)
                if value is not None:
                    if dp.date == index:
                        return value
            return None

        x = date
        x1 = find_left_index()
        x2 = find_right_index()
        y1 = find_val(x1)
        y2 = find_val(x2)
        if x2 == x1:
            return y1
        slope = (y2 - y1) / (x2 - x1)
        y_int = y1 - (slope * x1)
        y_to_find = slope * x + y_int

        return y_to_find

    def other_data_point_fill(self, date: int, dates: list[int], data_points: list,
                              goal_val: str, plots: list[Plot]) -> float:
        """
        Fill missing data point strategy which fills the missing data by fetching from other plots on the same date,
        or by searching a nearby (close to location of experiment) weather station dataset
        :param date: int - The date that needs to be filled
        :param dates: list[int] - The list of all dates that are known
        :param data_points: list[DataPoints] - The list of data points for the target plot to fill missing data for
        :param goal_val: str - The value name to target when finding a fill value
        :param plots: list[Plot] - List of plots to search from
        :return: float - Value filled from other plot at same date if found,
        otherwise the result of external_weather_data_fill(...)
        """
        for plot in plots:
            for dp in plot.data_points:
                if dp.date == date:
                    value = getattr(dp.conditions_state, goal_val, None)
                    if value is not None:
                        return value
        return self.external_weather_data_fill(plots[0].data_points[0].season_type, date, dates, data_points, goal_val)

    def external_weather_data_fill(self, season: str, date: int, dates, data_points, goal_val: str) -> float:
        """
        Fills in the weather data for a given date by reading from an external CSV file. If the specific value is not found,
        it falls back to a linear interpolation method.
        :param season: str - The season for which the weather data is required. Can be either "winter" or other seasons.
        :param date: int - The specific date for which the weather data is needed, represented as an integer.
        :param dates: A list or array of dates surrounding the target date, used for interpolation if necessary.
        :param data_points: A list or array of data points corresponding to the dates, used for interpolation if necessary.
        :param goal_val: str - The specific weather data parameter to retrieve (e.g., "temperature", "humidity").
        :return: The weather data value for the given date and parameter, as a float.
        """
        if season == "winter":
            file_path: str = "GapFillWeatherData/22PULSATW.csv"
        else:
            file_path: str = "GapFillWeatherData/22PULSATS.csv"

        with open(file_path, mode="r") as weather_file:
            csv_reader = csv.DictReader(weather_file)
            for row in csv_reader:
                fill_date: int = convert_str_to_int_date(row['date'])
                if fill_date == date:
                    if goal_val == "solar_radiation":  # Solar radiation units are different so skip
                        continue
                    if goal_val in row:
                        return float(row[goal_val])

        return self.lerp_fill(date, dates, data_points, goal_val)

    @staticmethod
    def insert_data_point(data_point, plot: Plot) -> None:
        """
        Inserts a new data point into a plot's data points in order (according to date)
        :param data_point: DataPoint - new data point to insert
        :param plot: Plot - plot with data points to insert into
        :return: None
        """
        insert_index = 0
        for i, dp in enumerate(plot.data_points):
            if data_point.date < dp.date:
                insert_index = i
                break
        plot.data_points.insert(insert_index, data_point)