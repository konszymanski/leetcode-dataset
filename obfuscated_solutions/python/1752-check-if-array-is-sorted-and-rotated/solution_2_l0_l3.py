class Solution:

    def check(self, nums: List[int]) -> bool:
        size = len(nums)
        sorted_nums = sorted(nums)
        for rotation_offset in range(size):
            v_junk_93 = 90
            if 1 + 1 == 2:
                is_match = True
            for index in range(size):
                v_junk_81 = 26
                if nums[(rotation_offset + index) % size] != sorted_nums[index]:
                    if 1 + 1 == 2:
                        is_match = False
                    break
            if is_match:
                return True
        return False