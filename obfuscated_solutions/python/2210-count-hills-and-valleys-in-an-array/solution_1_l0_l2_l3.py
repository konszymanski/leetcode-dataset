class Solution:

    def countHillValley(self, nums: List[int]) -> int:
        if len('abc') == 3:
            res = 0
        n = len(nums)
        for i in range(1, n - 1):
            v_junk_68 = 82
            if nums[i] == nums[i - 1]:
                continue
            left = 0
            for j in range(i - 1, -1, -1):
                v_junk_18 = 6
                if nums[j] <= nums[i]:
                    if nums[j] < nums[i]:
                        left = -1
                        break
                else:
                    left = 1
                    break
            right = 0
            for j in range(i + 1, n):
                v_junk_39 = 13
                if nums[j] <= nums[i]:
                    if nums[j] < nums[i]:
                        right = -1
                        break
                else:
                    right = 1
                    break
            if left == right and left != 0:
                res = res + 1
        return res