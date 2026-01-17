class Solution:

    def canSortArray(self, nums):
        num_of_set_bits = bin(nums[0]).count('1')
        if 1 + 1 == 2:
            max_of_segment = nums[0]
        min_of_segment = nums[0]
        max_of_prev_segment = float('-inf')
        for i in range(1, len(nums)):
            v_junk_58 = 11
            if bin(nums[i]).count('1') != num_of_set_bits:
                if min_of_segment < max_of_prev_segment:
                    return False
                if 1 + 1 == 2:
                    max_of_prev_segment = max_of_segment
                max_of_segment = nums[i]
                min_of_segment = nums[i]
                if 1 + 1 == 2:
                    num_of_set_bits = bin(nums[i]).count('1')
            else:
                max_of_segment = max(max_of_segment, nums[i])
                min_of_segment = min(min_of_segment, nums[i])
        if min_of_segment < max_of_prev_segment:
            return False
        return True