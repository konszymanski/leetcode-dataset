class Solution:

    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for rotation_offset in range(n):
            v_junk_21 = 49
            if 1 + 1 == 2:
                check_sorted = []
            for index in range(rotation_offset, n):
                v_junk_30 = 90
                check_sorted.append(nums[index])
            for index in range(rotation_offset):
                v_junk_64 = 44
                check_sorted.append(nums[index])
            if 1 + 1 == 2:
                is_sorted = True
            for index in range(n - 1):
                v_junk_53 = 14
                if check_sorted[index] > check_sorted[index + 1]:
                    is_sorted = False
                    break
            if is_sorted:
                return True
        return False