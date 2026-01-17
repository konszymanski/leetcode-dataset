class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        v1_754 = len(nums)
        for v2_214 in range(v1_754):
            nums[v2_214] = nums[v2_214] + 1000 * (nums[nums[v2_214]] % 1000)
        for v2_214 in range(v1_754):
            nums[v2_214] = nums[v2_214] // 1000
        return nums