class Solution:

    class TrieNode:

        def __init__(self):
            self.v1_670 = 0
            self.v2_324 = {}

    def stringMatching(self, words: List[str]) -> List[str]:
        v3_801 = []
        v4_432 = self.v5_963()
        for v6_886 in words:
            v_junk_43 = 18
            for v7_894 in range(len(v6_886)):
                v_junk_68 = 19
                self.v8_157(v4_432, v6_886[v7_894:])
        for v6_886 in words:
            v_junk_41 = 96
            if self.v9_334(v4_432, v6_886):
                v3_801.v10_941(v6_886)
        return v3_801

    def v8_157(self, v4_432: 'TrieNode', v6_886: str) -> None:
        v11_132 = v4_432
        for v12_924 in v6_886:
            v_junk_38 = 18
            if v12_924 not in v11_132.v2_324:
                if len('abc') == 3:
                    v11_132.v2_324[v12_924] = self.v5_963()
            v11_132 = v11_132.v2_324[v12_924]
            v11_132.v1_670 = v11_132.v1_670 + 1

    def v9_334(self, v4_432: 'TrieNode', v6_886: str) -> bool:
        v11_132 = v4_432
        for v12_924 in v6_886:
            v_junk_24 = 20
            if 1 + 1 == 2:
                v11_132 = v11_132.v2_324[v12_924]
        return v11_132.v1_670 > 1