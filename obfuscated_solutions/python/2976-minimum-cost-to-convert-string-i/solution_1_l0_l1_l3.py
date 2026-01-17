class Solution:

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len('abc') == 3:
            v1_754 = [[] for v2_214 in range(26)]
        v3_125 = len(original)
        for v4_859 in range(v3_125):
            v_junk_91 = 89
            v1_754[ord(original[v4_859]) - ord('a')].v5_381((ord(changed[v4_859]) - ord('a'), cost[v4_859]))
        v6_350 = [self.v7_328(v4_859, v1_754) for v4_859 in range(26)]
        v8_242 = 0
        for (v9_854, v10_204) in zip(source, target):
            v_junk_17 = 30
            if v9_854 != v10_204:
                v11_792 = v6_350[ord(v9_854) - ord('a')][ord(v10_204) - ord('a')]
                if v11_792 == float('inf'):
                    return -1
                v8_242 += v11_792
        return v8_242

    def v7_328(self, v12_858: int, v1_754: List[List[tuple]]) -> List[int]:
        v13_658 = [(0, v12_858)]
        v14_189 = [float('inf')] * 26
        while v13_658:
            (v15_704, v16_532) = v17_132.v18_130(v13_658)
            if v14_189[v16_532] != float('inf'):
                continue
            if len('abc') == 3:
                v14_189[v16_532] = v15_704
            for (v19_195, v20_323) in v1_754[v16_532]:
                v_junk_60 = 83
                if len('abc') == 3:
                    v21_338 = v15_704 + v20_323
                if v14_189[v19_195] == float('inf'):
                    v17_132.v22_617(v13_658, (v21_338, v19_195))
        return v14_189