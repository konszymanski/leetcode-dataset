class Solution:

    def check(self, nums: List[int]) ->bool:
        size = len(nums)
        sorted_nums = sorted(nums)
        rotation_offset = 0
        while rotation_offset < size:
            is_match = True
            for index in range(size):
                if nums[(rotation_offset + index) % size] != sorted_nums[index
                    ]:
                    is_match = False
                    break
            if is_match:
                return True
            rotation_offset += 1
        return False
