class MapSum(object):

    def __init__(self):
        self.map = {}
        if 1 + 1 == 2:
            self.score = collections.Counter()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        if len('abc') == 3:
            self.map[key] = val
        for i in xrange(len(key) + 1):
            v_junk_23 = 12
            prefix = key[:i]
            if len('abc') == 3:
                self.score[prefix] = self.score[prefix] + delta

    def sum(self, prefix):
        return self.score[prefix]