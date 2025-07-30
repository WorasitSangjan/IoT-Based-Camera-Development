import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from matplotlib.lines import Line2D
from scipy.stats import pearsonr
from DataStructures.plot import Plot
from Helpers.utility import convert_int_to_str_date, spring_variety_map, winter_variety_map, \
    singleton, get_plot, get_min_date, get_max_date


@singleton
class Visualizer:
    def __init__(self):
        # Visual settings
        self.line_mode = True
        self.point_mode = False
        # Data selection
        self.show_cigreen0 = False
        self.show_cigreen = False
        self.show_evi2 = False
        self.show_gndvi0 = False
        self.show_gndvi = False
        self.show_ndvi = False
        self.show_rdvi = False
        self.show_savi = False
        self.show_sr = False
        self.show_air_temp = False
        self.show_dew_point = False
        self.show_relative_humidity = False
        self.show_soil_temp_2in = False
        self.show_soil_temp_8in = False
        self.show_precipitation = False
        self.show_solar_radiation = False
        # Result data selection
        self.show_heading_date = False
        self.show_plant_height = False
        self.show_test_pounds_per_bushel = False
        self.show_yield = False
        self.show_prediction = False

    def visualize_plots(self, plots: list[Plot], entry_bloc_pairs: list[tuple],
                        predictions=None) -> None:
        """
        Create a graph visualization of given plots' data
        :param plots: list[Plot] - List of all plots
        :param entry_bloc_pairs: list[tuple] - List of entry block pairs to create visualization for
        :param predictions: list[float] - Optional list of predictions from ML model
        :return: None
        """

        # Start graph figure
        if predictions is None:
            predictions = []
        plt.figure(figsize=(16, 8))
        predictions_patch = mpatches.Patch(color='papayawhip', label='Yield predictions')
        cigreen0_patch = mpatches.Patch(color='purple', label='cigreen0')
        cigreen_patch = mpatches.Patch(color='peru', label='cigreen')
        evi2_patch = mpatches.Patch(color='violet', label='evi2')
        gndvi0_patch = mpatches.Patch(color='indigo', label='gndvi0')
        gndvi_patch = mpatches.Patch(color='navy', label='gndvi')
        ndvi_patch = mpatches.Patch(color='springgreen', label='ndvi')
        rdvi_patch = mpatches.Patch(color='seagreen', label='rdvi')
        savi_patch = mpatches.Patch(color='darkkhaki', label='savi')
        sr_patch = mpatches.Patch(color='rosybrown', label='sr')
        air_temp_patch = mpatches.Patch(color='orange', label='Air Temp')
        dew_point_patch = mpatches.Patch(color='cyan', label='Dew point')
        relative_hum_patch = mpatches.Patch(color='teal', label='Relative humidity')
        soil_temp_2in_patch = mpatches.Patch(color='brown', label='Soil Temp 2in')
        soil_temp_8in_patch = mpatches.Patch(color='yellow', label='Soil Temp 8in')
        precip_patch = mpatches.Patch(color='gray', label='Precipitation')
        solar_rad_patch = mpatches.Patch(color='pink', label='Solar radiation')
        heading_date_patch = mpatches.Patch(color='blue', label='Heading date')
        plant_height_patch = mpatches.Patch(color='green', label='Plant height')
        test_pounds_per_bushel_patch = mpatches.Patch(color='coral', label='Lbs/bushel')
        yield_patch = mpatches.Patch(color='darkgreen', label='Yield')
        handles = []
        dates = []
        if self.show_prediction:
            handles.append(predictions_patch)
        if self.show_cigreen0:
            handles.append(cigreen0_patch)
        if self.show_cigreen:
            handles.append(cigreen_patch)
        if self.show_evi2:
            handles.append(evi2_patch)
        if self.show_gndvi0:
            handles.append(gndvi0_patch)
        if self.show_gndvi:
            handles.append(gndvi_patch)
        if self.show_ndvi:
            handles.append(ndvi_patch)
        if self.show_rdvi:
            handles.append(rdvi_patch)
        if self.show_savi:
            handles.append(savi_patch)
        if self.show_sr:
            handles.append(sr_patch)
        if self.show_air_temp:
            handles.append(air_temp_patch)
        if self.show_dew_point:
            handles.append(dew_point_patch)
        if self.show_relative_humidity:
            handles.append(relative_hum_patch)
        if self.show_soil_temp_2in:
            handles.append(soil_temp_2in_patch)
        if self.show_soil_temp_8in:
            handles.append(soil_temp_8in_patch)
        if self.show_precipitation:
            handles.append(precip_patch)
        if self.show_solar_radiation:
            handles.append(solar_rad_patch)
        if self.show_heading_date:
            handles.append(heading_date_patch)
        if self.show_plant_height:
            handles.append(plant_height_patch)
        if self.show_test_pounds_per_bushel:
            handles.append(test_pounds_per_bushel_patch)
        if self.show_yield:
            handles.append(yield_patch)

        # Initialize vars
        min_date = 0
        max_date = 0
        offset = 0
        season = ""
        for pair in entry_bloc_pairs:
            # Get correct plot
            plot = get_plot(pair[0], pair[1], plots)
            if plot.data_points[0].season_type == "winter":
                var = winter_variety_map[plot.variety_index - 1]
            else:
                var = spring_variety_map[plot.variety_index - 1]
                season = "spring"
            print(f'Variety: {var}')

            # Lists to hold each data values
            dates = []
            cigreen0s = []
            cigreens = []
            evi2s = []
            gndvi0s = []
            gndvis = []
            ndvis = []
            rdvis = []
            savis = []
            srs = []
            air_temps = []
            dew_points = []
            relative_hums = []
            soil_temp_2ins = []
            soil_temp_8ins = []
            precip_means = []
            solar_rads = []

            # Get min and max range dates of graph
            min_date = get_min_date(plots)
            max_date = plot.data_points[len(plot.data_points) - 1].date

            # Get plot data
            for dp in plot.data_points:
                dates.append(dp.date)
                if self.show_cigreen0:
                    cigreen0s.append(dp.vi_state.cigreen0)
                if self.show_cigreen:
                    cigreens.append(dp.vi_state.cigreen)
                if self.show_evi2:
                    evi2s.append(dp.vi_state.evi2)
                if self.show_gndvi0:
                    gndvi0s.append(dp.vi_state.gndvi0)
                if self.show_gndvi:
                    gndvis.append(dp.vi_state.gndvi)
                if self.show_ndvi:
                    ndvis.append(dp.vi_state.ndvi)
                if self.show_rdvi:
                    rdvis.append(dp.vi_state.rdvi)
                if self.show_savi:
                    savis.append(dp.vi_state.savi)
                if self.show_sr:
                    srs.append(dp.vi_state.sr)
                if self.show_air_temp:
                    air_temps.append(dp.conditions_state.air_temp)
                if self.show_dew_point:
                    dew_points.append(dp.conditions_state.dewpoint)
                if self.show_relative_humidity:
                    relative_hums.append(dp.conditions_state.relative_humidity)
                if self.show_soil_temp_2in:
                    soil_temp_2ins.append(dp.conditions_state.soil_temp_2in)
                if self.show_soil_temp_8in:
                    soil_temp_8ins.append(dp.conditions_state.soil_temp_8in)
                if self.show_precipitation:
                    precip_means.append(dp.conditions_state.precipitation)
                if self.show_solar_radiation:
                    solar_rads.append(dp.conditions_state.solar_radiation)

            # Prediction bar graphs (first so that it is behind other graph values)
            if self.show_prediction and predictions:
                for date in dates:
                    index = dates.index(date)
                    plt.bar(date, predictions[index], color='papayawhip')

            # Point graphs
            if self.point_mode:
                for date in dates:
                    index = dates.index(date)
                    # VI means
                    if self.show_cigreen0:
                        plt.scatter(date, cigreen0s[index], color='purple')
                    if self.show_cigreen:
                        plt.scatter(date, cigreens[index], color='peru')
                    if self.show_evi2:
                        plt.scatter(date, evi2s[index], color='violet')
                    if self.show_gndvi0:
                        plt.scatter(date, gndvi0s[index], color='indigo')
                    if self.show_gndvi:
                        plt.scatter(date, gndvis[index], color='navy')
                    if self.show_ndvi:
                        plt.scatter(date, ndvis[index], color='springgreen')
                    if self.show_rdvi:
                        plt.scatter(date, rdvis[index], color='seagreen')
                    if self.show_savi:
                        plt.scatter(date, savis[index], color='darkkhaki')
                    if self.show_sr:
                        plt.scatter(date, srs[index], color='rosybrown')
                    # Air temp
                    if self.show_air_temp:
                        plt.scatter(date, air_temps[index], color='orange')
                    # Dew point
                    if self.show_dew_point:
                        plt.scatter(date, dew_points[index], color='cyan')
                    # Relative humidity
                    if self.show_relative_humidity:
                        plt.scatter(date, relative_hums[index], color='teal')
                    # Soil temp 2 in
                    if self.show_soil_temp_2in:
                        plt.scatter(date, soil_temp_2ins[index], color='brown')
                    # Soil temp 8 in
                    if self.show_soil_temp_8in:
                        plt.scatter(date, soil_temp_8ins[index], color='yellow')
                    # Precipitation
                    if self.show_precipitation:
                        plt.scatter(date, precip_means[index], color='gray')
                    # Solar radiation
                    if self.show_solar_radiation:
                        plt.scatter(date, solar_rads[index], color='pink')

            # Line graphs
            if self.line_mode:
                if self.show_cigreen0:
                    plt.plot(dates, cigreen0s, color='purple')
                if self.show_cigreen:
                    plt.plot(dates, cigreens, color='peru')
                if self.show_evi2:
                    plt.plot(dates, evi2s, color='violet')
                if self.show_gndvi0:
                    plt.plot(dates, gndvi0s, color='indigo')
                if self.show_gndvi:
                    plt.plot(dates, gndvis, color='navy')
                if self.show_ndvi:
                    plt.plot(dates, ndvis, color='springgreen')
                if self.show_rdvi:
                    plt.plot(dates, rdvis, color='seagreen')
                if self.show_savi:
                    plt.plot(dates, savis, color='darkkhaki')
                if self.show_sr:
                    plt.plot(dates, srs, color='rosybrown')
                if self.show_air_temp:
                    plt.plot(dates, air_temps, color='orange')
                if self.show_dew_point:
                    plt.plot(dates, dew_points, color='cyan')
                if self.show_relative_humidity:
                    plt.plot(dates, relative_hums, color='teal')
                if self.show_soil_temp_2in:
                    plt.plot(dates, soil_temp_2ins, color='brown')
                if self.show_soil_temp_8in:
                    plt.plot(dates, soil_temp_8ins, color='yellow')
                if self.show_precipitation:
                    plt.plot(dates, precip_means, color='gray')
                if self.show_solar_radiation:
                    plt.plot(dates, solar_rads, color='pink')

            # Heading date
            if self.show_heading_date:
                plt.scatter(plot.heading_date, 0, color='blue')
                print("Heading date: ", end="")
                print(convert_int_to_str_date(plot.heading_date))

            # Plant height
            if self.show_plant_height:
                plt.bar(max_date + 20 + offset, plot.plant_height, color='green')

            # Test pounds per bushel
            if self.show_test_pounds_per_bushel:
                plt.bar(max_date + 10 + offset, plot.test_pounds_per_bushel, color='coral')

            # Yield
            if self.show_yield:
                plt.bar(max_date + offset, plot.crop_yield, color='darkgreen')
                print(f'Actual yield: {plot.crop_yield}')
                offset += 1
            if self.show_prediction and predictions:
                print(f'Final expected yield: {round(predictions[len(predictions) - 1], 2)}')
                error_amts = [abs(plot.crop_yield - prediction) for prediction in predictions]
                best_index = error_amts.index(min(error_amts))
                best_date = min_date + best_index
                print(f'Best expected yield: {round(predictions[best_index], 2)}')
                print(f'Best expected yield date: {best_date} or {convert_int_to_str_date(best_date)}')

        # Graph logic
        current_ticks = plt.gca().get_xticks()
        temp_ticks = [int(val) for val in current_ticks]
        str_dates = [convert_int_to_str_date(num) for num in temp_ticks]
        label_dict = {key: value for key, value in zip(temp_ticks, str_dates)}
        new_labels = [label_dict.get(tick, '') for tick in current_ticks]
        plt.xticks(ticks=current_ticks, labels=new_labels)
        if self.show_plant_height:
            plt.xlim(min_date, max_date + 21 + offset)
        elif self.show_test_pounds_per_bushel:
            plt.xlim(min_date, max_date + 11 + offset)
        else:
            plt.xlim(min_date, max_date + 1 + offset)
        # Make title string
        title_str: str = "Values for Plots: "
        for pair in entry_bloc_pairs:
            if season == 'spring':
                variety = spring_variety_map[pair[0] - 1]
            else:
                variety = winter_variety_map[pair[0] - 1]
            title_str += str(pair) + " " + variety + " "
        plt.title(title_str)
        plt.xlabel('Dates')
        plt.ylabel('Plot Values')
        plt.grid(True)
        plt.legend(handles=handles, loc="upper left")
        plt.tight_layout()
        plt.show()

    def visualize_variety(self, plots: list[Plot], target_variety: str) -> None:
        """
        Visualize all plots of a given variety
        :param plots: list[Plot] - List of all plots
        :param target_variety: str - Variety name to show visualization for
        :return: None
        """
        season = plots[0].data_points[0].season_type
        entry_bloc_pairs = []
        for plot in plots:
            if season == 'spring':
                variety_str = spring_variety_map[plot.variety_index - 1]
            else:
                variety_str = winter_variety_map[plot.variety_index - 1]
            if variety_str == target_variety:
                entry_bloc_pairs.append((plot.variety_index, plot.replication_variety))

        self.visualize_by_plots(plots, entry_bloc_pairs)

    def visualize_num_plots(self, plots: list[Plot], num: int) -> None:
        entry_bloc_pairs = []
        total = 0
        for plot in plots:
            if total >= num:
                break
            total += 1
            entry_bloc_pairs.append((plot.variety_index, plot.replication_variety))

        self.visualize_by_plots(plots, entry_bloc_pairs)

    def visualize_by_plots(self, plots: list[Plot], entry_bloc_pairs: list[tuple]) -> None:
        """
        Create a graph visualization of given plots' data coloring by each plot
        :param plots: list[Plot] - List of all plots
        :param entry_bloc_pairs: list[tuple] - List of entry block pairs to create visualization for
        :return: None
        """

        # Start graph figure
        plt.figure(figsize=(16, 8))

        # Initialize colormap
        num_pairs = len(entry_bloc_pairs)
        colormap = plt.get_cmap('hsv', num_pairs + 1)

        # Initialize vars
        min_date = 0
        max_date = 0
        offset = 0
        for idx, pair in enumerate(entry_bloc_pairs):
            # Get correct plot
            plot = get_plot(pair[0], pair[1], plots)

            # Lists to hold each data values
            dates = []
            cigreen0s = []
            cigreens = []
            evi2s = []
            gndvi0s = []
            gndvis = []
            ndvis = []
            rdvis = []
            savis = []
            srs = []
            air_temps = []
            dew_points = []
            relative_hums = []
            soil_temp_2ins = []
            soil_temp_8ins = []
            precip_means = []
            solar_rads = []

            # Get min and max range dates of graph
            min_date = get_min_date(plots)
            max_date = get_max_date(plots)

            # Get plot data
            for dp in plot.data_points:
                if dp.date > max_date:
                    break
                dates.append(dp.date)
                if self.show_cigreen0:
                    cigreen0s.append(dp.vi_state.cigreen0)
                if self.show_cigreen:
                    cigreens.append(dp.vi_state.cigreen)
                if self.show_evi2:
                    evi2s.append(dp.vi_state.evi2)
                if self.show_gndvi0:
                    gndvi0s.append(dp.vi_state.gndvi0)
                if self.show_gndvi:
                    gndvis.append(dp.vi_state.gndvi)
                if self.show_ndvi:
                    ndvis.append(dp.vi_state.ndvi)
                if self.show_rdvi:
                    rdvis.append(dp.vi_state.rdvi)
                if self.show_savi:
                    savis.append(dp.vi_state.savi)
                if self.show_sr:
                    srs.append(dp.vi_state.sr)
                if self.show_air_temp:
                    air_temps.append(dp.conditions_state.air_temp)
                if self.show_dew_point:
                    dew_points.append(dp.conditions_state.dewpoint)
                if self.show_relative_humidity:
                    relative_hums.append(dp.conditions_state.relative_humidity)
                if self.show_soil_temp_2in:
                    soil_temp_2ins.append(dp.conditions_state.soil_temp_2in)
                if self.show_soil_temp_8in:
                    soil_temp_8ins.append(dp.conditions_state.soil_temp_8in)
                if self.show_precipitation:
                    precip_means.append(dp.conditions_state.precipitation)
                if self.show_solar_radiation:
                    solar_rads.append(dp.conditions_state.solar_radiation)

            # Generate color for the current plot
            plot_color = colormap(idx / num_pairs)

            # Point graphs
            if self.point_mode:
                for date in dates:
                    index = dates.index(date)
                    # VI means
                    if self.show_cigreen0:
                        plt.scatter(date, cigreen0s[index], color=plot_color)
                    if self.show_cigreen:
                        plt.scatter(date, cigreens[index], color=plot_color)
                    if self.show_evi2:
                        plt.scatter(date, evi2s[index], color=plot_color)
                    if self.show_gndvi0:
                        plt.scatter(date, gndvi0s[index], color=plot_color)
                    if self.show_gndvi:
                        plt.scatter(date, gndvis[index], color=plot_color)
                    if self.show_ndvi:
                        plt.scatter(date, ndvis[index], color=plot_color)
                    if self.show_rdvi:
                        plt.scatter(date, rdvis[index], color=plot_color)
                    if self.show_savi:
                        plt.scatter(date, savis[index], color=plot_color)
                    if self.show_sr:
                        plt.scatter(date, srs[index], color=plot_color)
                    # Air temp
                    if self.show_air_temp:
                        plt.scatter(date, air_temps[index], color=plot_color)
                    # Dew point
                    if self.show_dew_point:
                        plt.scatter(date, dew_points[index], color=plot_color)
                    # Relative humidity
                    if self.show_relative_humidity:
                        plt.scatter(date, relative_hums[index], color=plot_color)
                    # Soil temp 2 in
                    if self.show_soil_temp_2in:
                        plt.scatter(date, soil_temp_2ins[index], color=plot_color)
                    # Soil temp 8 in
                    if self.show_soil_temp_8in:
                        plt.scatter(date, soil_temp_8ins[index], color=plot_color)
                    # Precipitation
                    if self.show_precipitation:
                        plt.scatter(date, precip_means[index], color=plot_color)
                    # Solar radiation
                    if self.show_solar_radiation:
                        plt.scatter(date, solar_rads[index], color=plot_color)

            # Line graphs
            if self.line_mode:
                if self.show_cigreen0:
                    plt.plot(dates, cigreen0s, color=plot_color)
                if self.show_cigreen:
                    plt.plot(dates, cigreens, color=plot_color)
                if self.show_evi2:
                    plt.plot(dates, evi2s, color=plot_color)
                if self.show_gndvi0:
                    plt.plot(dates, gndvi0s, color=plot_color)
                if self.show_gndvi:
                    plt.plot(dates, gndvis, color=plot_color)
                if self.show_ndvi:
                    plt.plot(dates, ndvis, color=plot_color)
                if self.show_rdvi:
                    plt.plot(dates, rdvis, color=plot_color)
                if self.show_savi:
                    plt.plot(dates, savis, color=plot_color)
                if self.show_sr:
                    plt.plot(dates, srs, color=plot_color)
                if self.show_air_temp:
                    plt.plot(dates, air_temps, color=plot_color)
                if self.show_dew_point:
                    plt.plot(dates, dew_points, color=plot_color)
                if self.show_relative_humidity:
                    plt.plot(dates, relative_hums, color=plot_color)
                if self.show_soil_temp_2in:
                    plt.plot(dates, soil_temp_2ins, color=plot_color)
                if self.show_soil_temp_8in:
                    plt.plot(dates, soil_temp_8ins, color=plot_color)
                if self.show_precipitation:
                    plt.plot(dates, precip_means, color=plot_color)
                if self.show_solar_radiation:
                    plt.plot(dates, solar_rads, color=plot_color)
            # Plot
            print(f'Plot variety: {plot.variety_index}, replication: {plot.replication_variety}')

            # Heading date
            if self.show_heading_date:
                plt.scatter(plot.heading_date, 0, color=plot_color)
                print("Heading date: ", end="")
                print(convert_int_to_str_date(plot.heading_date))

            # Plant height
            if self.show_plant_height:
                plt.bar(max_date + 20 + offset, plot.plant_height, color=plot_color)

            # Test pounds per bushel
            if self.show_test_pounds_per_bushel:
                plt.bar(max_date + 10 + offset, plot.test_pounds_per_bushel, color=plot_color)

            # Yield
            if self.show_yield:
                plt.bar(max_date + offset, plot.crop_yield / 200, color=plot_color)
                print(f'Actual yield: {plot.crop_yield}')
                offset += 1

        # Graph logic
        current_ticks = plt.gca().get_xticks()
        temp_ticks = [int(val) for val in current_ticks]
        str_dates = [convert_int_to_str_date(num) for num in temp_ticks]
        label_dict = {key: value for key, value in zip(temp_ticks, str_dates)}
        new_labels = [label_dict.get(tick, '') for tick in current_ticks]
        plt.xticks(ticks=current_ticks, labels=new_labels)
        if self.show_plant_height:
            plt.xlim(min_date, max_date + 21 + offset)
        elif self.show_test_pounds_per_bushel:
            plt.xlim(min_date, max_date + 11 + offset)
        else:
            plt.xlim(min_date, max_date + 1 + offset)

        # Make title string
        title_str: str = "Values for Plots: "
        for pair in entry_bloc_pairs:
            title_str += str(pair) + " "
        plt.title(title_str)
        plt.xlabel('Dates')
        plt.ylabel('Plot Values')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def visualize_avg_correspondence(plots: list[Plot], val_type: str) -> None:
        """
        Create a graph of the correspondence between the average value type and the yield
        :param val_type: str - The type of value type to view correspondence for
        :param plots: list[Plot] - list of plots to create correspondence from
        :return: None
        """
        def get_avg_val(data_points: list, start_i, end_i):
            total = 0
            count = 0
            for i in range(start_i, end_i):
                if count >= end_i - start_i:
                    break
                count += 1
                if hasattr(data_points[i], val_type):
                    total += getattr(data_points[i], val_type)
                if hasattr(data_points[i].conditions_state, val_type):
                    total += getattr(data_points[i].conditions_state, val_type)
                if hasattr(data_points[i].vi_state, val_type):
                    total += getattr(data_points[i].vi_state, val_type)
            return total / count

        season = plots[0].data_points[0].season_type
        # Define a color map based on variety_index
        color_map = {
            0: 'red',
            1: 'green',
            2: 'blue',
            3: 'purple',
            4: 'orange',
            5: 'yellow',
            6: 'gray',
            7: 'salmon',
            8: 'pink',
            9: 'wheat',
            10: 'teal',
            11: 'cyan'
        }

        # Best vals
        best_corr = 0
        best_split_size = 0
        best_offset = 0

        # Loop to search all correlations
        split_size = 50
        while split_size > 49:
            split_offset = 0
            while split_size + split_offset <= 50:
                vi_avgs = []
                yields = []
                for p in plots:
                    vi_avgs.append(get_avg_val(p.data_points, split_offset, split_offset + split_size))
                    yields.append(p.crop_yield)
                # Pearson Correlation
                pearson_corr, _ = pearsonr(vi_avgs, yields)
                if abs(pearson_corr) > abs(best_corr):
                    best_corr = pearson_corr
                    best_split_size = split_size
                    best_offset = split_offset
                split_offset += 1
            split_size -= 1

        print(f'Best split size: {best_split_size}')
        print(f'Best offset: {best_offset}')
        print(f'Best correlation: {best_corr}')

        val_avgs = []
        yields = []
        colors = []
        for p in plots:
            colors.append(color_map.get(p.variety_index - 1, 'black'))
            val_avgs.append(get_avg_val(p.data_points, best_offset, best_offset + best_split_size))
            yields.append(p.crop_yield)

        # Create the plot
        plt.figure(figsize=(16, 8))
        plt.scatter(val_avgs, yields, c=colors, marker='o')

        # Create custom legend handles
        if season == "winter":
            trimmed_color_map = {k: v for k, v in list(color_map.items())[:8]}
            legend_elements = [
                Line2D([0], [0], marker='o', color='w', markerfacecolor=color,
                       markersize=10, label=f'{winter_variety_map[i]}')
                for i, color in trimmed_color_map.items()
            ]
        else:
            legend_elements = [
                Line2D([0], [0], marker='o', color='w', markerfacecolor=color,
                       markersize=10, label=f'{spring_variety_map[i]}')
                for i, color in color_map.items()
            ]
        plt.legend(handles=legend_elements, title="Variety Index")

        # Customize the plot
        plt.xlabel('Value Averages')
        plt.ylabel('Yields')
        plt.title('Value to Yield')
        plt.tight_layout()
        plt.grid(True)

        # Display the plot
        plt.show()

    @staticmethod
    def visualize_heading_date_correlation(plots: list[Plot], val_type: str) -> None:
        """
        Create a graph of the correspondence between the given value type at the heading date and the yield
        :param val_type: str - The type of value type to view heading correspondence for
        :param plots: list[Plot] - list of plots to create correspondence from
        :return: None
        """
        def get_vi_at_heading_date(data_points: list, heading_date: int):
            for dp in data_points:
                if dp.date == heading_date:
                    if hasattr(dp, val_type):
                        return getattr(dp, val_type)
                    if hasattr(dp.conditions_state, val_type):
                        return getattr(dp.conditions_state, val_type)
                    if hasattr(dp.vi_state, val_type):
                        return getattr(dp.vi_state, val_type)
            return None

        season = plots[0].data_points[0].season_type
        # Define a color map based on variety_index
        color_map = {
            0: 'red',
            1: 'green',
            2: 'blue',
            3: 'purple',
            4: 'orange',
            5: 'yellow',
            6: 'gray',
            7: 'salmon',
            8: 'pink',
            9: 'wheat',
            10: 'teal',
            11: 'cyan'
        }

        vals = []
        yields = []
        colors = []
        for p in plots:
            colors.append(color_map.get(p.variety_index - 1, 'black'))
            vals.append(get_vi_at_heading_date(p.data_points, p.heading_date))
            yields.append(p.crop_yield)

        # Pearson Correlation
        pearson_corr, _ = pearsonr(vals, yields)
        print(f'Value at heading date correlation: {pearson_corr}')

        # Create the plot
        plt.figure(figsize=(16, 8))
        plt.scatter(vals, yields, c=colors, marker='o')

        # Create custom legend handles
        if season == "winter":
            trimmed_color_map = {k: v for k, v in list(color_map.items())[:8]}
            legend_elements = [
                Line2D([0], [0], marker='o', color='w', markerfacecolor=color,
                       markersize=10, label=f'{winter_variety_map[i]}')
                for i, color in trimmed_color_map.items()
            ]
        else:
            legend_elements = [
                Line2D([0], [0], marker='o', color='w', markerfacecolor=color,
                       markersize=10, label=f'{spring_variety_map[i]}')
                for i, color in color_map.items()
            ]
        plt.legend(handles=legend_elements, title="Variety Index")

        # Customize the plot
        plt.xlabel('Value at Heading date')
        plt.ylabel('Yields')
        plt.title('Value to Yield')
        plt.tight_layout()
        plt.grid(True)

        # Display the plot
        plt.show()
