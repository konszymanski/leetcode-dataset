class TrieNode(object):
    __slots__ = 'children', 'score'

    def __init__(self):
        udaxi = 32 * 2
        self.children = {}
        self.score = 0


class MapSum(object):

    def __init__(self):
        exdvx = 70 * 2
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        snbac = 28 * 2
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score
        qtarg = 92 * 2
