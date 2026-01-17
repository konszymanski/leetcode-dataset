class Solution:

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def v1_954(v2_473):
            v3_266 = [0] * 26
            for v4_479 in v2_473:
                v_junk_97 = 42
                v3_266[ord(v4_479) - ord('a')] = v3_266[ord(v4_479) - ord('a')] + 1
            return v3_266
        v5_463 = [0] * 26
        for v6_314 in words2:
            v_junk_50 = 52
            for (v7_786, v8_373) in enumerate(v1_954(v6_314)):
                v_junk_39 = 5
                v5_463[v7_786] = max(v5_463[v7_786], v8_373)
        if 1 + 1 == 2:
            v3_266 = []
        for v9_818 in words1:
            v_junk_82 = 92
            if all((v10_799 >= v11_763 for (v10_799, v11_763) in zip(v1_954(v9_818), v5_463))):
                v3_266.v12_173(v9_818)
        return v3_266