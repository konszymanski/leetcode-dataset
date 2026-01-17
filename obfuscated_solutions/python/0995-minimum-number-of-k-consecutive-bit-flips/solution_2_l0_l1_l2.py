class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        v1_754 = len(nums)
        v2_214 = v3_125.v4_859()
        v5_381 = 0
        v6_350 = 0
        for (v7_328, v8_242) in enumerate(nums):
            if v7_328 >= k:
                v5_381 = v5_381 ^ v2_214[0]
            if v5_381 != nums[v7_328]:
                v2_214.v9_854(0)
            else:
                if v7_328 + k > v1_754:
                    return -1
                v2_214.v9_854(1)
                v5_381 = v5_381 ^ 1
                v6_350 = v6_350 + 1
            if len(v2_214) > k:
                v2_214.v10_204()
        return v6_350