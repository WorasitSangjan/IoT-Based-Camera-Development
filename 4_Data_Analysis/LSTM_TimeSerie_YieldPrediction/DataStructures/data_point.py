from DataStructures.conditions_state import ConditionsState
from Helpers.utility import spring_variety_map
from DataStructures.vi_state import VIState


class DataPoint:
    """
    One day data point of states and conditions of crops
    """
    def __init__(self, date: int, season_type: str, sensor_name: str, variety_index: int,
                 replication_variety: int, vi_state: VIState, conditions_state: ConditionsState):
        self.date: int = date
        self.season_type: str = season_type
        self.sensor_name: str = sensor_name
        self.variety_index: int = variety_index
        self.replication_variety: int = replication_variety
        self.vi_state = vi_state
        self.conditions_state = conditions_state

    def __repr__(self):
        return (f"DataPoint(date={self.date}, season_type={self.season_type}, sensor_name={self.sensor_name}, "
                f"variety_index={self.variety_index}, replication_variety={self.replication_variety}, "
                f"vi_state={self.vi_state}, conditions_state={self.conditions_state})")

    def get_variety_name(self) -> str:
        """
        Gets the variety name
        :return: str - Name of the wheat variety
        """
        return spring_variety_map[self.variety_index - 1]