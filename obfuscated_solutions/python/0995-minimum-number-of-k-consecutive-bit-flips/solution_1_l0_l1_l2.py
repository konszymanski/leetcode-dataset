class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        v1_754 = [False] * len(nums)
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(len(nums)):
            if v4_859 >= k:
                if v1_754[v4_859 - k]:
                    v2_214 = v2_214 - 1
            if v2_214 % 2 == nums[v4_859]:
                if v4_859 + k > len(nums):
                    return -1
                v2_214 = v2_214 + 1
                v1_754[v4_859] = True
                v3_125 = v3_125 + 1
        return v3_125