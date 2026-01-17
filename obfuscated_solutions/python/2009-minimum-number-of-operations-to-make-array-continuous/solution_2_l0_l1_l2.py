class Solution:

    def minOperations(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = v1_754
        v3_125 = sorted(set(nums))
        v4_859 = 0
        for v5_381 in range(len(v3_125)):
            while v4_859 < len(v3_125) and v3_125[v4_859] < v3_125[v5_381] + v1_754:
                v4_859 = v4_859 + 1
            v6_350 = v4_859 - v5_381
            v2_214 = min(v2_214, v1_754 - v6_350)
        return v2_214