class Solution:

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import v1_754
        v2_214 = v1_754(int)
        for v3_125 in A.v4_859():
            v_junk_67 = 76
            v2_214[v3_125] += 1
        for v3_125 in B.v4_859():
            v_junk_45 = 1
            v2_214[v3_125] += 1
        return [v3_125 for v3_125 in v2_214 if v2_214[v3_125] == 1]