import csv
import pandas as pd

from Helpers.utility import convert_str_to_int_date, singleton
from Helpers.interpolator import Interpolator
from Helpers.visualizer import Visualizer

from DataStructures.conditions_state import ConditionsState
from DataStructures.data_point import DataPoint
from DataStructures.plot import Plot
from DataStructures.vi_state import VIState

visualizer = Visualizer()


@singleton
class Parser:
    def __init__(self) -> None:
        self.interpolator = Interpolator()

    def parse_data(self, season: str, plots: list) -> None:
        """
        Parses the given season data provided in PullmanIOTData
        :param season: str - Target season data to parse
        :param plots: list - List of plots to parse into
        :return: None
        """
        # Ground truth
        file_path: str = f'PullmanIOTData/GT_{season}_wheat.csv'

        with open(file_path, mode="r") as gt_file:
            csv_reader = csv.DictReader(gt_file)
            for row in csv_reader:
                type_name = row['Name1']
                heading_date = int(row['Heading Date'])
                plant_height = float(row['Plant height inch'])
                test_pounds_per_bushel = float(row['Test Wt lb/bu'])
                plot_area = int(row['Plot Area'])
                if plot_area > 80:  # Skip the large areas because the no IOT data for them
                    continue
                experiment_name = row['Experiment Name']
                year = int(row['Year'])
                location = row['Locn']
                variety_index = int(row['ENTRY'])
                if int(row['BLOC']) > 3:  # No IOT data exists for BLOC's 4-6 for winter data
                    continue
                replication_variety = int(row['BLOC'])
                crop_yield = float(row['Yield bu/a'])
                plot = Plot(type_name, heading_date, plant_height, test_pounds_per_bushel, plot_area, experiment_name,
                            year, location, variety_index, replication_variety, crop_yield)
                plots.append(plot)

        # Full Wheat Data
        file_path = f'PullmanIOTData/Final_{season.capitalize()}_Wheat_Weather.csv'
        temp_target_vi = "sr"  # Used to make sure loop only adds one data point per day
        with open(file_path, mode="r") as dp_file:
            csv_reader = csv.DictReader(dp_file)
            for row in csv_reader:
                # DataPoint specific
                date = convert_str_to_int_date(row['date'])
                season_type = row['wheat']
                sensor_name = row['sensor']
                variety_index = int(row['variety'])
                replication_variety = int(row['rep_var'])
                # VI class in DataPoint
                vi_formula = row['vi']
                if vi_formula != temp_target_vi:
                    continue
                vi_state = VIState()
                # Conditions class in DataPoint
                air_temp = float(row['air_temp'])
                dew_point = float(row['dewpoint'])
                relative_humidity = float(row['rel_humidity'])
                soil_temp_2in = float(row['soil_temp_2_in'])
                soil_temp_8in = float(row['avg_soil_temp_8_in'])
                precipitation = float(row['precip'])
                solar_radiation = float(row['solar_rad'])
                conditions_state = ConditionsState(air_temp, dew_point, relative_humidity, soil_temp_2in,
                                                   soil_temp_8in, precipitation, solar_radiation)
                # Add the DataPoint to the Plots data
                data_point = DataPoint(date, season_type, sensor_name, variety_index,
                                       replication_variety, vi_state, conditions_state)
                plots[self.get_data_point_index(data_point, plots)].add_data_point(data_point)

        with open(file_path, mode="r") as dp_file:
            csv_reader = csv.DictReader(dp_file)
            for row in csv_reader:
                date = convert_str_to_int_date(row['date'])
                variety_index = int(row['variety'])
                replication_variety = int(row['rep_var'])
                vi_formula = row['vi']
                vi_mean = float(row['mean'])
                vi_state = None
                found = False
                for p in plots:
                    if found:
                        break
                    if p.replication_variety == replication_variety and p.variety_index == variety_index:
                        for dp in p.data_points:
                            if dp.date == date:
                                vi_state = dp.vi_state
                                break
                setattr(vi_state, vi_formula, vi_mean)

        # Filter faulty plots:
        plots_to_rm = []
        for plot in plots:
            if len(plot.data_points) == 0:
                plots_to_rm.append(plot)
        for p in plots_to_rm:
            plots.remove(p)

        for plot in plots:
            self.sort_data_points_by_date(plot.data_points)
        self.interpolator.fill_missing_data(plots)

    @staticmethod
    def sort_data_points_by_date(data_points: list) -> list:
        """
        Sorts data points by their date
        :param data_points: list[DataPoint] - data point list to sort
        :return: list[DataPoint] - sorted list of data points
        """

        def partition(lst, low, high):
            pivot = lst[high].date
            i = low - 1
            for j in range(low, high):
                if lst[j].date <= pivot:
                    i += 1
                    lst[i], lst[j] = lst[j], lst[i]
            lst[i + 1], lst[high] = lst[high], lst[i + 1]
            return i + 1

        def quick_sort(lst, low, high):
            if low < high:
                pi = partition(lst, low, high)
                quick_sort(lst, low, pi - 1)
                quick_sort(lst, pi + 1, high)

        quick_sort(data_points, 0, len(data_points) - 1)
        return data_points

    @staticmethod
    def get_data_point_index(data_point, plots: list[Plot]) -> int:
        """
        Gets the index of the plot that should hold the specific given data point
        :param plots: List[Plots] - List to find the index in
        :param data_point: DataPoint
        :return: int - index for data_point, -1 if none found, or -2 if multiple found
        """
        count = 0
        index = 0

        for i, plot in enumerate(plots):
            if plot.replication_variety == data_point.replication_variety and \
                    plot.variety_index == data_point.variety_index:
                count += 1
                index = i

        if count == 0:
            raise Exception("No data points with given parameters in plots")
            # return -1
        elif count > 1:
            raise Exception("More than one data point with given parameters in plots")
            # return -2
        else:
            return index
