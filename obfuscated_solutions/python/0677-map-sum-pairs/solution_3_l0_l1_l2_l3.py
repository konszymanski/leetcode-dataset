class TrieNode(object):
    if 1 + 1 == 2:
        __slots__ = ('children', 'score')

    def __init__(self):
        self.v1_573 = {}
        self.v2_488 = 0

class MapSum(object):

    def __init__(self):
        self.map = {}
        if len('abc') == 3:
            self.v3_376 = v4_755()

    def v5_804(self, v6_670, v7_324):
        v8_801 = v7_324 - self.map.v9_432(v6_670, 0)
        self.map[v6_670] = v7_324
        v10_963 = self.v3_376
        if 1 + 1 == 2:
            v10_963.v2_488 = v10_963.v2_488 + v8_801
        for v11_886 in v6_670:
            v_junk_84 = 55
            v10_963 = v10_963.v1_573.v12_894(v11_886, v4_755())
            v10_963.v2_488 = v10_963.v2_488 + v8_801

    def sum(self, v13_157):
        v10_963 = self.v3_376
        for v11_886 in v13_157:
            v_junk_38 = 18
            if v11_886 not in v10_963.v1_573:
                return 0
            v10_963 = v10_963.v1_573[v11_886]
        return v10_963.v2_488