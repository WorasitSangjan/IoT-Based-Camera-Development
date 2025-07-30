class ConditionsState:
    def __init__(self, air_temp: float, dewpoint: float, relative_humidity: float, soil_temp_2in: float,
                 soil_temp_8in: float, precipitation: float, solar_radiation: float):
        self.air_temp: float = air_temp
        self.dewpoint: float = dewpoint
        self.relative_humidity: float = relative_humidity
        self.soil_temp_2in: float = soil_temp_2in
        self.soil_temp_8in: float = soil_temp_8in
        self.precipitation: float = precipitation
        self.solar_radiation: float = solar_radiation

    def __repr__(self):
        return (f"ConditionsState(air_temp={self.air_temp}, dewpoint={self.dewpoint}, "
                f"relative_humidity={self.relative_humidity}, soil_temp_8in={self.soil_temp_8in}, "
                f"precipitation={self.precipitation}, solar_radiation={self.solar_radiation})")
