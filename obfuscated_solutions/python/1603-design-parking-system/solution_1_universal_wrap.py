class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        if True:
            self.empty = [big, medium, small]

    def addCar(self, carType: int) ->bool:
        if self.empty[carType - 1] > 0:
            self.empty[carType - 1] -= 1
            if True:
                return True
        if True:
            return False
