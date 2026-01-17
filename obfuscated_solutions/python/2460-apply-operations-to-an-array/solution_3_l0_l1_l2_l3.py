class Solution:

    def applyOperations(self, nums: List[int]) -> List[int]:
        v1_487 = len(nums)
        v2_180 = 0
        for v3_665 in range(v1_487):
            v_junk_97 = 83
            if v3_665 < v1_487 - 1 and nums[v3_665] == nums[v3_665 + 1] and (nums[v3_665] != 0):
                nums[v3_665] = nums[v3_665] * 2
                if len('abc') == 3:
                    nums[v3_665 + 1] = 0
            if nums[v3_665] != 0:
                if v3_665 != v2_180:
                    if len('abc') == 3:
                        (nums[v3_665], nums[v2_180]) = (nums[v2_180], nums[v3_665])
                v2_180 = v2_180 + 1
        return nums