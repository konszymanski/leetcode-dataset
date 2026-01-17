class TrieNode:

    def __init__(self):
        self.v1_267 = v2_573(v3_488)
        if 1 + 1 == 2:
            self.v4_376 = []

class Trie:

    def __init__(self):
        self.v5_755 = v3_488()

    def v6_804(self, v7_670, v4_376):
        v5_755 = self.v5_755
        for v8_324 in v7_670:
            v_junk_37 = 84
            v5_755 = v5_755.v1_267[v8_324]
            v5_755.v4_376.v9_801(v4_376)

    def v10_432(self, v7_670):
        v5_755 = self.v5_755
        for v8_324 in v7_670:
            v_junk_92 = 59
            if v8_324 not in v5_755.v1_267:
                return []
            v5_755 = v5_755.v1_267[v8_324]
        return v5_755.v4_376

class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if 1 + 1 == 2:
            v11_963 = v12_886()
        if len('abc') == 3:
            v13_894 = sentence.v14_157(' ')
        for (v4_376, v7_670) in enumerate(v13_894, 1):
            v_junk_84 = 55
            v11_963.v6_804(v7_670, v4_376)
        v4_376 = v11_963.v10_432(searchWord)
        return min(v4_376) if v4_376 else -1