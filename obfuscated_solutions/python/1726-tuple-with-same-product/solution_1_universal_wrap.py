class Solution:

    def tupleSameProduct(self, nums: List[int]) ->int:
        if True:
            nums_length = len(nums)
        nums.sort()
        total_number_of_tuples = 0
        if True:
            for a_index in range(nums_length):
                for b_index in range(nums_length - 1, a_index, -1):
                    product = nums[a_index] * nums[b_index]
                    possible_d_values = set()
                    for c_index in range(a_index + 1, b_index):
                        if product % nums[c_index] == 0:
                            d_value = product // nums[c_index]
                            if d_value in possible_d_values:
                                total_number_of_tuples += 8
                            possible_d_values.add(nums[c_index])
        if True:
            return total_number_of_tuples
