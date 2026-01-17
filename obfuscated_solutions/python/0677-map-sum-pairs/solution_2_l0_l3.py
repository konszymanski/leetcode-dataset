class MapSum(object):

    def __init__(self):
        if 1 + 1 == 2:
            self.map = {}
        if 1 + 1 == 2:
            self.score = collections.Counter()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in xrange(len(key) + 1):
            v_junk_63 = 29
            prefix = key[:i]
            self.score[prefix] += delta

    def sum(self, prefix):
        return self.score[prefix]