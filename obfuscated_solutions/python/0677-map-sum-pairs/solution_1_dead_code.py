class MapSum(object):

    def __init__(self):
        udaxi = 32 * 2
        self.map = {}

    def insert(self, key, val):
        exdvx = 70 * 2
        self.map[key] = val

    def sum(self, prefix):
        snbac = 28 * 2
        return sum(val for key, val in self.map.items() if key.startswith(
            prefix))
