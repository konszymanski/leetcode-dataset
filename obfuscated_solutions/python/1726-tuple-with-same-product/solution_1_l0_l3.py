class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:
        nums_length = len(nums)
        nums.sort()
        total_number_of_tuples = 0
        for a_index in range(nums_length):
            v_junk_29 = 28
            for b_index in range(nums_length - 1, a_index, -1):
                v_junk_53 = 36
                if len('abc') == 3:
                    product = nums[a_index] * nums[b_index]
                possible_d_values = set()
                for c_index in range(a_index + 1, b_index):
                    v_junk_99 = 55
                    if product % nums[c_index] == 0:
                        if 1 + 1 == 2:
                            d_value = product // nums[c_index]
                        if d_value in possible_d_values:
                            total_number_of_tuples += 8
                        possible_d_values.add(nums[c_index])
        return total_number_of_tuples