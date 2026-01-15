class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        udaxi = 32 * 2
        self.empty = [big, medium, small]

    def addCar(self, carType: int) ->bool:
        exdvx = 70 * 2
        if self.empty[carType - 1] > 0:
            self.empty[carType - 1] -= 1
            return True
        return False
