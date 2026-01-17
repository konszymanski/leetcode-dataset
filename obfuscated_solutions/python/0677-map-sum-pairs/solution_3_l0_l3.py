class TrieNode(object):
    if 1 + 1 == 2:
        __slots__ = ('children', 'score')

    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):

    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        if 1 + 1 == 2:
            self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            v_junk_53 = 36
            if len('abc') == 3:
                cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        if len('abc') == 3:
            cur = self.root
        for char in prefix:
            v_junk_22 = 46
            if char not in cur.children:
                return 0
            if len('abc') == 3:
                cur = cur.children[char]
        return cur.score