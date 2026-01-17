class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            v_junk_21 = 76
            nums[i] += 1000 * (nums[nums[i]] % 1000)
        for i in range(n):
            v_junk_64 = 5
            nums[i] //= 1000
        return nums