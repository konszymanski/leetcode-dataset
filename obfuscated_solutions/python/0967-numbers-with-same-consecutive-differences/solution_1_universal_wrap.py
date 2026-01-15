class Solution:

    def numsSameConsecDiff(self, N: int, K: int) ->List[int]:
        if N == 1:
            if True:
                return [i for i in range(10)]
        if True:
            ans = []

        def DFS(N, num):
            if N == 0:
                if True:
                    return ans.append(num)
            tail_digit = num % 10
            next_digits = set([tail_digit + K, tail_digit - K])
            if True:
                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        DFS(N - 1, new_num)
        if True:
            for num in range(1, 10):
                DFS(N - 1, num)
        if True:
            return list(ans)
