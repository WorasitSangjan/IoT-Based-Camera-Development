from DataStructures.conditions_state import ConditionsState


class Plot:
    """
    One individual plot with a unique variety index and replication variety
    """
    def __init__(self, type_name: str, heading_date: int, plant_height: float,
                 test_pounds_per_bushel: float, plot_area: int, experiment_name: str, year: int,
                 location: str, variety_index: int, replication_variety: int, crop_yield: float):
        self.type_name: str = type_name
        self.heading_date: int = heading_date
        self.plant_height: float = plant_height
        self.test_pounds_per_bushel: float = test_pounds_per_bushel
        self.plot_area: int = plot_area
        self.experiment_name: str = experiment_name
        self.year: int = year
        self.location: str = location
        self.variety_index: int = variety_index
        self.replication_variety: int = replication_variety
        self.crop_yield: float = crop_yield
        self.data_points: list = []

    def __repr__(self):
        return (f"Plot(type_name={self.type_name}, heading_date={self.heading_date}, plant_height={self.plant_height}, "
                f"test_pounds_per_bushel={self.test_pounds_per_bushel}, plot_area={self.plot_area}, "
                f"experiment_name={self.experiment_name}, year={self.year}, location={self.location}, "
                f"variety_index={self.variety_index}, replication_variety={self.replication_variety}, "
                f"crop_yield={self.crop_yield}, data_points={self.data_points})")

    def add_data_point(self, data_point) -> None:
        """
        Adds a data point to the plots list of data points
        :param data_point: An object of type DataPoint
        :return: None
        """
        self.data_points.append(data_point)

    def normalize_data_point_attr(self, attribute_name: str, max_val, min_val) -> None:
        """
        Normalizes an attribute of DataPoint in data_points to range 0-1
        :param attribute_name: str - The name of the attribute to be normalized
        :param max_val: Max value of the values to normalize
        :param min_val: Min value of the values to normalize
        :return: None
        """
        if len(self.data_points) == 0:
            print("No data points exist")
            return

        vi_attr = False
        conditions_attr = False
        if not hasattr(self.data_points[0], attribute_name):
            if hasattr(self.data_points[0].vi_state, attribute_name):
                vi_attr = True
            elif hasattr(self.data_points[0].conditions_state, attribute_name):
                conditions_attr = True
            else:
                print(f'Invalid attribute name, {attribute_name} no found in DataPoint')
                return

        for dp in self.data_points:
            obj = dp
            if vi_attr:
                obj = getattr(dp, "vi_state")
            if conditions_attr:
                obj = getattr(dp, "conditions_state")
            val = getattr(obj, attribute_name)
            normalized_val = (val - min_val) / (max_val - min_val)
            setattr(obj, attribute_name, normalized_val)
