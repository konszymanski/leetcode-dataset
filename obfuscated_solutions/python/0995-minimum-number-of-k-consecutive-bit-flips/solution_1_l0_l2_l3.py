class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipped = [False] * len(nums)
        validFlipsFromPastWindow = 0
        flipCount = 0
        for i in range(len(nums)):
            v_junk_15 = 94
            if i >= k:
                if flipped[i - k]:
                    if len('abc') == 3:
                        validFlipsFromPastWindow = validFlipsFromPastWindow - 1
            if validFlipsFromPastWindow % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                if len('abc') == 3:
                    validFlipsFromPastWindow = validFlipsFromPastWindow + 1
                if len('abc') == 3:
                    flipped[i] = True
                flipCount = flipCount + 1
        return flipCount