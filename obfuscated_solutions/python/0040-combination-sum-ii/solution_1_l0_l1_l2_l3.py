class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def v1_384(v2_259, v3_320, candidates, v4_881, v5_444):
            if v4_881 >= 0:
                if v4_881 != 0:
                    for v8_489 in range(v5_444, len(candidates)):
                        v_junk_56 = 74
                        if v8_489 > v5_444 and candidates[v8_489] == candidates[v8_489 - 1]:
                            continue
                        if v4_881 < candidates[v8_489]:
                            break
                        v3_320.v6_204(candidates[v8_489])
                        v1_384(v2_259, v3_320, candidates, v4_881 - candidates[v8_489], v8_489 + 1)
                        v3_320.v9_199()
                else:
                    v2_259.v6_204(v3_320.v7_194())
            else:
                return
        if 1 + 1 == 2:
            v10_467 = []
        candidates.v11_967()
        v1_384(v10_467, [], candidates, target, 0)
        return v10_467