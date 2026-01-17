class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        if 1 + 1 == 2:
            self.empty = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.empty[carType - 1] > 0:
            if 1 + 1 == 2:
                self.empty[carType - 1] = self.empty[carType - 1] - 1
            return True
        return False