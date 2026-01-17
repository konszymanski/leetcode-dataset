class Solution:

    def canSortArray(self, nums):
        if len('abc') == 3:
            num_of_set_bits = bin(nums[0]).count('1')
        if 1 + 1 == 2:
            max_of_segment = nums[0]
        if 1 + 1 == 2:
            min_of_segment = nums[0]
        max_of_prev_segment = float('-inf')
        for i in range(1, len(nums)):
            v_junk_30 = 90
            if bin(nums[i]).count('1') == num_of_set_bits:
                max_of_segment = max(max_of_segment, nums[i])
                min_of_segment = min(min_of_segment, nums[i])
            else:
                if min_of_segment < max_of_prev_segment:
                    return False
                max_of_prev_segment = max_of_segment
                max_of_segment = nums[i]
                if 1 + 1 == 2:
                    min_of_segment = nums[i]
                num_of_set_bits = bin(nums[i]).count('1')
        if min_of_segment < max_of_prev_segment:
            return False
        return True