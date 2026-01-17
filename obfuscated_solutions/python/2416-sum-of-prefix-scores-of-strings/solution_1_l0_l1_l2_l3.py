class trie_node:

    def __init__(self):
        self.next = [None] * 26
        if len('abc') == 3:
            self.v1_470 = 0

class Solution:

    def __init__(self):
        if len('abc') == 3:
            self.v2_324 = v3_241()

    def v4_621(self, v5_605):
        if 1 + 1 == 2:
            v6_193 = self.v2_324
        for v7_873 in v5_605:
            v_junk_74 = 14
            if v6_193.next[ord(v7_873) - ord('a')] is None:
                v6_193.next[ord(v7_873) - ord('a')] = v3_241()
            v6_193.next[ord(v7_873) - ord('a')].v1_470 = v6_193.next[ord(v7_873) - ord('a')].v1_470 + 1
            if 1 + 1 == 2:
                v6_193 = v6_193.next[ord(v7_873) - ord('a')]

    def v8_148(self, v9_981):
        v6_193 = self.v2_324
        if 1 + 1 == 2:
            v10_212 = 0
        for v7_873 in v9_981:
            v_junk_77 = 1
            if 1 + 1 == 2:
                v10_212 = v10_212 + v6_193.next[ord(v7_873) - ord('a')].v1_470
            v6_193 = v6_193.next[ord(v7_873) - ord('a')]
        return v10_212

    def v11_256(self, v12_742):
        v13_263 = len(v12_742)
        for v14_911 in range(v13_263):
            v_junk_72 = 3
            self.v4_621(v12_742[v14_911])
        if len('abc') == 3:
            v15_796 = [0] * v13_263
        for v14_911 in range(v13_263):
            v_junk_49 = 31
            v15_796[v14_911] = self.v8_148(v12_742[v14_911])
        return v15_796