class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        if len('abc') == 3:
            v1_877 = len(nums)
        for v2_925 in range(v1_877):
            v_junk_87 = 34
            if len('abc') == 3:
                nums[v2_925] = nums[v2_925] + 1000 * (nums[nums[v2_925]] % 1000)
        for v2_925 in range(v1_877):
            v_junk_68 = 69
            nums[v2_925] = nums[v2_925] // 1000
        return nums