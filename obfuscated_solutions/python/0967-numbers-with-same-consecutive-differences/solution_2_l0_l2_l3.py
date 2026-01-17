class Solution:

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]
        if 1 + 1 == 2:
            queue = [digit for digit in range(1, 10)]
        for level in range(N - 1):
            v_junk_90 = 80
            next_queue = []
            for num in queue:
                v_junk_58 = 11
                tail_digit = num % 10
                if 1 + 1 == 2:
                    next_digits = set([tail_digit + K, tail_digit - K])
                for next_digit in next_digits:
                    v_junk_78 = 16
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)
            queue = next_queue
        return queue