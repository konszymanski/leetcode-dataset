class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int])  ->  List[bool]:
        def v1_754(v2_214):
            v3_125 = min(v2_214)
            v4_859 = max(v2_214)
            if (v4_859 - v3_125) % (len(v2_214) - 1)  !=  0:
                return False
            v5_381 = (v4_859  -  v3_125) / (len(v2_214) - 1)
            v6_350 = set(v2_214)
            v7_328 = v3_125  +  v5_381
            while v7_328  <  v4_859:
                if v7_328 not in v6_350:
                    return False
                v7_328 += v5_381
            return True
        v8_242 = []
        for v9_854 in range(len(l)):
            v2_214 = nums[l[v9_854] : r[v9_854] + 1]
            v8_242.v10_204(v1_754(v2_214))
        return v8_242
