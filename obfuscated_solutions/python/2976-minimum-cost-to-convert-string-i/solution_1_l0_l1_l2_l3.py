class Solution:

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        v1_569 = [[] for v2_246 in range(26)]
        v3_371 = len(original)
        for v4_242 in range(v3_371):
            v_junk_53 = 15
            v1_569[ord(original[v4_242]) - ord('a')].v5_352((ord(changed[v4_242]) - ord('a'), cost[v4_242]))
        if 1 + 1 == 2:
            v6_862 = [self.v7_674(v4_242, v1_569) for v4_242 in range(26)]
        v8_651 = 0
        for (v9_369, v10_864) in zip(source, target):
            v_junk_43 = 65
            if v9_369 != v10_864:
                v11_698 = v6_862[ord(v9_369) - ord('a')][ord(v10_864) - ord('a')]
                if v11_698 == float('inf'):
                    return -1
                v8_651 = v8_651 + v11_698
        return v8_651

    def v7_674(self, v12_538: int, v1_569: List[List[tuple]]) -> List[int]:
        v13_697 = [(0, v12_538)]
        v14_508 = [float('inf')] * 26
        while v13_697:
            if len('abc') == 3:
                (v15_470, v16_324) = v17_241.v18_621(v13_697)
            if v14_508[v16_324] != float('inf'):
                continue
            v14_508[v16_324] = v15_470
            for (v19_605, v20_193) in v1_569[v16_324]:
                v_junk_35 = 20
                v21_873 = v15_470 + v20_193
                if v14_508[v19_605] == float('inf'):
                    v17_241.v22_148(v13_697, (v21_873, v19_605))
        return v14_508