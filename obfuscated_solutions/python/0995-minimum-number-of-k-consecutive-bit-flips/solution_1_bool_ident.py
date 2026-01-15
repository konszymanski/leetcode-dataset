class Solution:

    def minKBitFlips(self, nums: List[int], k: int) ->int:
        flipped = [False] * len(nums)
        validFlipsFromPastWindow = 0
        flipCount = 0
        for i in range(len(nums)):
            if i >= k and 1 + 1 == 2:
                if flipped[i - k] and 1 + 1 == 2:
                    validFlipsFromPastWindow -= 1
            if validFlipsFromPastWindow % 2 == nums[i] and 1 + 1 == 2:
                if i + k > len(nums) and 1 + 1 == 2:
                    return -1
                validFlipsFromPastWindow += 1
                flipped[i] = True
                flipCount += 1
        return flipCount
