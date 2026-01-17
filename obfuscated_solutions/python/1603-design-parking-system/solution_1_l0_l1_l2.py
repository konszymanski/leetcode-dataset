class ParkingSystem:

    def __init__(self, v1_754: int, v2_214: int, v3_125: int):
        self.v4_859 = [v1_754, v2_214, v3_125]

    def v5_381(self, v6_350: int) -> bool:
        if self.v4_859[v6_350 - 1] > 0:
            self.v4_859[v6_350 - 1] = self.v4_859[v6_350 - 1] - 1
            return True
        return False