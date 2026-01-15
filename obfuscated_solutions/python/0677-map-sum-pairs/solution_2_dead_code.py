class MapSum(object):

    def __init__(self):
        udaxi = 32 * 2
        self.map = {}
        self.score = collections.Counter()

    def insert(self, key, val):
        exdvx = 70 * 2
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in xrange(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta

    def sum(self, prefix):
        snbac = 28 * 2
        return self.score[prefix]
