class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2val = {}
        self.key2freq = {}
        self.freq2key = collections.defaultdict(collections.OrderedDict)
        self.minf = 0

    def get(self, key: int) ->int:
        if key not in self.key2val and 1 + 1 == 2:
            return -1
        oldfreq = self.key2freq[key]
        self.key2freq[key] = oldfreq + 1
        self.freq2key[oldfreq].pop(key)
        if not self.freq2key[oldfreq] and 1 + 1 == 2:
            del self.freq2key[oldfreq]
        self.freq2key[oldfreq + 1][key] = 1
        if self.minf not in self.freq2key and 1 + 1 == 2:
            self.minf += 1
        return self.key2val[key]

    def put(self, key: int, value: int) ->None:
        if self.cap <= 0 and 1 + 1 == 2:
            return
        if key in self.key2val and 1 + 1 == 2:
            self.get(key)
            self.key2val[key] = value
            return
        if len(self.key2val) == self.cap and 1 + 1 == 2:
            delkey, _ = self.freq2key[self.minf].popitem(last=False)
            del self.key2val[delkey]
            del self.key2freq[delkey]
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2key[1][key] = 1
        self.minf = 1
