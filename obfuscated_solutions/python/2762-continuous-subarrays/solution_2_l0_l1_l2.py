class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        v1_754 = []
        v2_214 = []
        v3_125 = v4_859 = 0
        v5_381 = 0
        while v4_859 < len(nums):
            v6_350.v7_328(v1_754, (nums[v4_859], v4_859))
            v6_350.v7_328(v2_214, (-nums[v4_859], v4_859))
            while v3_125 < v4_859 and -v2_214[0][0] - v1_754[0][0] > 2:
                v3_125 = v3_125 + 1
                while v1_754 and v1_754[0][1] < v3_125:
                    v6_350.v8_242(v1_754)
                while v2_214 and v2_214[0][1] < v3_125:
                    v6_350.v8_242(v2_214)
            v5_381 = v5_381 + (v4_859 - v3_125 + 1)
            v4_859 = v4_859 + 1
        return v5_381