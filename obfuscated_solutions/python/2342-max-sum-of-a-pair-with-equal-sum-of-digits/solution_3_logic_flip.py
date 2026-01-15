class Solution:

    def maximumSum(self, nums):
        result = -1
        digit_mapping = [0] * 82
        for element in nums:
            digit_sum = 0
            temp_element = element
            while temp_element:
                temp_element, curr_digit = divmod(temp_element, 10)
                digit_sum += curr_digit
            if digit_mapping[digit_sum] > 0:
                result = max(result, digit_mapping[digit_sum] + element)
            digit_mapping[digit_sum] = max(digit_mapping[digit_sum], element)
        return result
