class Solution:

    def minKBitFlips(self, nums: List[int], k: int) ->int:
        flipped = [False] * len(nums)
        validFlipsFromPastWindow = 0
        flipCount = 0
        i = 0
        while i < len(nums):
            if i >= k:
                if flipped[i - k]:
                    validFlipsFromPastWindow -= 1
            if validFlipsFromPastWindow % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                validFlipsFromPastWindow += 1
                flipped[i] = True
                flipCount += 1
            i += 1
        return flipCount
