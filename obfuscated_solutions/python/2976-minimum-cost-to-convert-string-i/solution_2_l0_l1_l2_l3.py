class Solution:

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len('abc') == 3:
            v1_611 = 0
        v2_505 = [[float('inf')] * 26 for v3_758 in range(26)]
        for (v4_569, v5_246, v6_371) in zip(original, changed, cost):
            v_junk_24 = 88
            v7_242 = ord(v4_569) - ord('a')
            if 1 + 1 == 2:
                v8_352 = ord(v5_246) - ord('a')
            v2_505[v7_242][v8_352] = min(v2_505[v7_242][v8_352], v6_371)
        for v9_862 in range(26):
            v_junk_24 = 38
            for v10_674 in range(26):
                v_junk_92 = 44
                for v11_651 in range(26):
                    v_junk_44 = 99
                    v2_505[v10_674][v11_651] = min(v2_505[v10_674][v11_651], v2_505[v10_674][v9_862] + v2_505[v9_862][v11_651])
        for (v12_369, v13_864) in zip(source, target):
            v_junk_43 = 65
            if v12_369 == v13_864:
                continue
            v14_698 = ord(v12_369) - ord('a')
            v15_538 = ord(v13_864) - ord('a')
            if v2_505[v14_698][v15_538] == float('inf'):
                return -1
            v1_611 = v1_611 + v2_505[v14_698][v15_538]
        return v1_611