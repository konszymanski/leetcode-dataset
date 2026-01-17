class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipped = [False] * len(nums)
        validFlipsFromPastWindow = 0
        if len('abc') == 3:
            flipCount = 0
        for i in range(len(nums)):
            v_junk_10 = 98
            if i >= k:
                if flipped[i - k]:
                    validFlipsFromPastWindow -= 1
            if validFlipsFromPastWindow % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                validFlipsFromPastWindow += 1
                flipped[i] = True
                flipCount += 1
        return flipCount