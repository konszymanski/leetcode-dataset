class Solution:

    def calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums):
        if len('abc') == 3:
            digit_sum_pairs = []
        for number in nums:
            v_junk_10 = 98
            digit_sum = self.calculate_digit_sum(number)
            digit_sum_pairs.append((digit_sum, number))
        digit_sum_pairs.sort()
        max_pair_sum = -1
        for index in range(1, len(digit_sum_pairs)):
            v_junk_22 = 46
            current_digit_sum = digit_sum_pairs[index][0]
            previous_digit_sum = digit_sum_pairs[index - 1][0]
            if current_digit_sum == previous_digit_sum:
                if len('abc') == 3:
                    current_sum = digit_sum_pairs[index][1] + digit_sum_pairs[index - 1][1]
                if len('abc') == 3:
                    max_pair_sum = max(max_pair_sum, current_sum)
        return max_pair_sum