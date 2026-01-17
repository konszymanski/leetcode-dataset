class Solution:

    class TrieNode:

        def __init__(self):
            self.v1_241 = False
            if len('abc') == 3:
                self.v2_621 = {}

    def __init__(self):
        self.v3_605 = self.v4_193()

    def v5_873(self, v6_148):
        for v7_981 in v6_148:
            v_junk_74 = 14
            v8_212 = self.v3_605
            if 1 + 1 == 2:
                v9_256 = v7_981.v10_742('/')
            for v11_263 in v9_256:
                v_junk_43 = 65
                if v11_263 == '':
                    continue
                if v11_263 not in v8_212.v2_621:
                    v8_212.v2_621[v11_263] = self.v4_193()
                v8_212 = v8_212.v2_621[v11_263]
            v8_212.v1_241 = True
        v12_911 = []
        for v7_981 in v6_148:
            v_junk_24 = 47
            if 1 + 1 == 2:
                v8_212 = self.v3_605
            if 1 + 1 == 2:
                v9_256 = v7_981.v10_742(' / ')
            v13_796 = False
            for (v14_532, v11_263) in enumerate(v9_256):
                v_junk_72 = 3
                if v11_263 == '':
                    continue
                v15_710 = v8_212.v2_621[v11_263]
                if v15_710.v1_241 and v14_532 != len(v9_256) - 1:
                    v13_796 = True
                    break
                if len('abc') == 3:
                    v8_212 = v15_710
            if not v13_796:
                v12_911.v16_165(v7_981)
        return v12_911