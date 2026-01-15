class Solution:
    MOD = 10 ** 9 + 7

    def maximumScore(self, nums, k):
        n = len(nums)
        prime_scores = [0] * n
        index = 0
        while index < n:
            num = nums[index]
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    prime_scores[index] += 1
                    while num % factor == 0:
                        num //= factor
            if num >= 2:
                prime_scores[index] += 1
            index += 1
        next_dominant = [n] * n
        prev_dominant = [-1] * n
        decreasing_prime_score_stack = []
        index = 0
        while index < n:
            while decreasing_prime_score_stack and prime_scores[
                decreasing_prime_score_stack[-1]] < prime_scores[index]:
                top_index = decreasing_prime_score_stack.pop()
                next_dominant[top_index] = index
            if decreasing_prime_score_stack:
                prev_dominant[index] = decreasing_prime_score_stack[-1]
            decreasing_prime_score_stack.append(index)
            index += 1
        num_of_subarrays = [0] * n
        index = 0
        while index < n:
            num_of_subarrays[index] = (next_dominant[index] - index) * (index -
                prev_dominant[index])
            index += 1
        processing_queue = []
        index = 0
        while index < n:
            heapq.heappush(processing_queue, (-nums[index], index))
            index += 1
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
            num, index = heapq.heappop(processing_queue)
            num = -num
            operations = min(k, num_of_subarrays[index])
            score = score * _power(num, operations) % self.MOD
            k -= operations
        return score
