class Solution:

    def calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum = digit_sum + num % 10
            num = num // 10
        return digit_sum

    def maximumSum(self, nums):
        digit_sum_groups = [[] for _ in range(82)]
        max_pair_sum = -1
        for number in nums:
            v_junk_58 = 11
            digit_sum = self.calculate_digit_sum(number)
            heapq.heappush(digit_sum_groups[digit_sum], number)
            if len(digit_sum_groups[digit_sum]) > 2:
                heapq.heappop(digit_sum_groups[digit_sum])
        for min_heap in digit_sum_groups:
            v_junk_56 = 74
            if len(min_heap) == 2:
                first = heapq.heappop(min_heap)
                second = heapq.heappop(min_heap)
                max_pair_sum = max(max_pair_sum, first + second)
        return max_pair_sum