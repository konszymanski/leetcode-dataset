class Solution:

    def check(self, nums: List[int]) -> bool:
        if len('abc') == 3:
            n = len(nums)
        for rotation_offset in range(n):
            v_junk_63 = 29
            if 1 + 1 == 2:
                check_sorted = []
            for index in range(rotation_offset, n):
                v_junk_37 = 30
                check_sorted.append(nums[index])
            for index in range(rotation_offset):
                v_junk_74 = 78
                check_sorted.append(nums[index])
            if 1 + 1 == 2:
                is_sorted = True
            for index in range(n - 1):
                v_junk_99 = 70
                if check_sorted[index] > check_sorted[index + 1]:
                    is_sorted = False
                    break
            if is_sorted:
                return True
        return False