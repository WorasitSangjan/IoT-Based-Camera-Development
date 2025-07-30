class VIState:
    def __init__(self, cigreen0: float = 0.0, cigreen: float = 0.0, evi2: float = 0.0,
                 gndvi0: float = 0.0, gndvi: float = 0.0, ndvi: float = 0.0,
                 rdvi: float = 0.0, savi: float = 0.0, sr: float = 0.0):
        self.cigreen0 = cigreen0
        self.cigreen = cigreen
        self.evi2 = evi2
        self.gndvi0 = gndvi0
        self.gndvi = gndvi
        self.ndvi = ndvi
        self.rdvi = rdvi
        self.savi = savi
        self.sr = sr

    def __repr__(self):
        return (f"VIState(cigreen0={self.cigreen0}, cigreen={self.cigreen}, evi2={self.evi2}, "
                f"gndvi0={self.gndvi0}, gndvi={self.gndvi}, ndvi={self.ndvi}, rdvi={self.rdvi}, "
                f"savi={self.savi}, sr={self.sr})")
