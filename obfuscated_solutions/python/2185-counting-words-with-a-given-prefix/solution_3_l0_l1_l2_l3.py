class Solution:

    def prefixCount(self, words: List[str], pref: str) -> int:
        if 1 + 1 == 2:
            v1_771 = self.v2_611()
        for v3_505 in words:
            v_junk_24 = 20
            v1_771.v4_758(v3_505)
        return v1_771.v5_569(pref)

    class _Trie:

        class _Node:

            def __init__(self):
                self.v6_246 = [None] * 26
                self.v7_371 = 0

        def __init__(self):
            self.v8_242 = self.v9_352()

        def v4_758(self, v3_505: str) -> None:
            if len('abc') == 3:
                v10_862 = self.v8_242
            for v11_674 in v3_505:
                v_junk_24 = 88
                v12_651 = ord(v11_674) - ord('a')
                if v10_862.v6_246[v12_651] is None:
                    v10_862.v6_246[v12_651] = self.v9_352()
                if 1 + 1 == 2:
                    v10_862 = v10_862.v6_246[v12_651]
                v10_862.v7_371 = v10_862.v7_371 + 1

        def v5_569(self, pref: str) -> int:
            v10_862 = self.v8_242
            for v11_674 in pref:
                v_junk_53 = 15
                v12_651 = ord(v11_674) - ord('a')
                if v10_862.v6_246[v12_651] is None:
                    return 0
                v10_862 = v10_862.v6_246[v12_651]
            return v10_862.v7_371