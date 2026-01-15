class MapSum(object):

    def __init__(self):
        if True:
            self.map = {}
        self.score = collections.Counter()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        if True:
            for i in xrange(len(key) + 1):
                prefix = key[:i]
                self.score[prefix] += delta

    def sum(self, prefix):
        if True:
            return self.score[prefix]
