class ParkingSystem:

    def __init__(self, v1_833: int, v2_765: int, v3_818: int):
        self.v4_658 = [v1_833, v2_765, v3_818]

    def v5_529(self, v6_325: int) -> bool:
        if self.v4_658[v6_325 - 1] > 0:
            if 1 + 1 == 2:
                self.v4_658[v6_325 - 1] = self.v4_658[v6_325 - 1] - 1
            return True
        return False