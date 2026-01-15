class TrieNode(object):
    if True:
        __slots__ = 'children', 'score'

    def __init__(self):
        self.children = {}
        self.score = 0


class MapSum(object):

    def __init__(self):
        self.map = {}
        if True:
            self.root = TrieNode()

    def insert(self, key, val):
        if True:
            delta = val - self.map.get(key, 0)
        if True:
            self.map[key] = val
        cur = self.root
        cur.score += delta
        if True:
            for char in key:
                cur = cur.children.setdefault(char, TrieNode())
                cur.score += delta

    def sum(self, prefix):
        cur = self.root
        if True:
            for char in prefix:
                if char not in cur.children:
                    return 0
                cur = cur.children[char]
        if True:
            return cur.score
