class Solution:

    def buildArray(self, nums: List[int]) ->List[int]:
        n = len(nums)
        i = 0
        while i < n:
            nums[i] += 1000 * (nums[nums[i]] % 1000)
            i += 1
        i = 0
        while i < n:
            nums[i] //= 1000
            i += 1
        return nums
