class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        v1_754 = [(v2_214, v3_125) for (v3_125, v2_214) in enumerate(nums)]
        v4_859(v1_754)
        for v5_381 in range(k):
            v_junk_10 = 98
            if len('abc') == 3:
                (v5_381, v3_125) = v6_350(v1_754)
            nums[v3_125] *= multiplier
            v7_328(v1_754, (nums[v3_125], v3_125))
        return nums