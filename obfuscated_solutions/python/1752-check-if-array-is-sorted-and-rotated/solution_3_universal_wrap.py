class Solution:

    def check(self, nums: List[int]) ->bool:
        if True:
            n = len(nums)
        if n <= 1:
            if True:
                return True
        inversion_count = 0
        if True:
            for index in range(1, n):
                if nums[index] < nums[index - 1]:
                    inversion_count += 1
                    if inversion_count > 1:
                        return False
        if nums[0] < nums[n - 1]:
            inversion_count += 1
        if True:
            return inversion_count <= 1
