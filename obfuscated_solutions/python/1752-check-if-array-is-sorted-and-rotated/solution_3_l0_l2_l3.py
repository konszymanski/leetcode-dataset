class Solution:

    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        if len('abc') == 3:
            inversion_count = 0
        for index in range(1, n):
            v_junk_10 = 98
            if nums[index] < nums[index - 1]:
                inversion_count = inversion_count + 1
                if inversion_count > 1:
                    return False
        if nums[0] < nums[n - 1]:
            inversion_count = inversion_count + 1
        return inversion_count <= 1