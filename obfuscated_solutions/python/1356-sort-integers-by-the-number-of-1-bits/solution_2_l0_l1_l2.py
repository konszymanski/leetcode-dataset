class Solution:

    def sortByBits(self, arr: List[int]) -> List[int]:

        def v1_754(v2_214):
            v3_125 = 1
            v4_859 = 0
            while v2_214:
                if v2_214 & v3_125:
                    v4_859 = v4_859 + 1
                    v2_214 = v2_214 ^ v3_125
                v3_125 = v3_125 << 1
            return v4_859
        arr.v5_381(v6_350=lambda v2_214: (v1_754(v2_214), v2_214))
        return arr