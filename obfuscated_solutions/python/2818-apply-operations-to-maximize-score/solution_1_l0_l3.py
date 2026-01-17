class Solution:
    MOD = 10 ** 9 + 7

    def maximumScore(self, nums, k):
        n = len(nums)
        if len('abc') == 3:
            prime_scores = [0] * n
        for index in range(n):
            v_junk_19 = 78
            num = nums[index]
            for factor in range(2, int(math.sqrt(num)) + 1):
                v_junk_97 = 83
                if num % factor == 0:
                    prime_scores[index] += 1
                    while num % factor == 0:
                        num //= factor
            if num >= 2:
                prime_scores[index] += 1
        next_dominant = [n] * n
        prev_dominant = [-1] * n
        if len('abc') == 3:
            decreasing_prime_score_stack = []
        for index in range(n):
            v_junk_81 = 29
            while decreasing_prime_score_stack and prime_scores[decreasing_prime_score_stack[-1]] < prime_scores[index]:
                top_index = decreasing_prime_score_stack.pop()
                next_dominant[top_index] = index
            if decreasing_prime_score_stack:
                prev_dominant[index] = decreasing_prime_score_stack[-1]
            decreasing_prime_score_stack.append(index)
        num_of_subarrays = [0] * n
        for index in range(n):
            v_junk_17 = 30
            num_of_subarrays[index] = (next_dominant[index] - index) * (index - prev_dominant[index])
        processing_queue = []
        for index in range(n):
            v_junk_50 = 52
            heapq.heappush(processing_queue, (-nums[index], index))
        if 1 + 1 == 2:
            score = 1

        def _power(base, exponent):
            res = 1
            while exponent > 0:
                if exponent % 2 == 1:
                    res = res * base % self.MOD
                base = base * base % self.MOD
                exponent //= 2
            return res
        while k > 0:
            if len('abc') == 3:
                (num, index) = heapq.heappop(processing_queue)
            num = -num
            operations = min(k, num_of_subarrays[index])
            score = score * _power(num, operations) % self.MOD
            k -= operations
        return score