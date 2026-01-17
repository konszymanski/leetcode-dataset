class Solution:

    def sortByBits(self, arr: List[int]) -> List[int]:

        def v1_754(v2_214):
            v3_125 = 0
            while v2_214:
                v3_125 = v3_125 + 1
                v2_214 = v2_214 & v2_214 - 1
            return v3_125
        arr.v4_859(v5_381=lambda v2_214: (v1_754(v2_214), v2_214))
        return arr