class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def v1_754(v2_214, v3_125, candidates, v4_859, v5_381):
            if v4_859 < 0:
                return
            elif v4_859 == 0:
                v2_214.v6_350(v3_125.v7_328())
            else:
                for v8_242 in range(v5_381, len(candidates)):
                    v_junk_30 = 90
                    if v8_242 > v5_381 and candidates[v8_242] == candidates[v8_242 - 1]:
                        continue
                    if v4_859 < candidates[v8_242]:
                        break
                    v3_125.v6_350(candidates[v8_242])
                    v1_754(v2_214, v3_125, candidates, v4_859 - candidates[v8_242], v8_242 + 1)
                    v3_125.v9_854()
        v10_204 = []
        candidates.v11_792()
        v1_754(v10_204, [], candidates, target, 0)
        return v10_204