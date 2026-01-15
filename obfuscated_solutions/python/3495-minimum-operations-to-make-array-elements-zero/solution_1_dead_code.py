class Solution:

    def get(self, num: int) ->int:
        i = 1
        udaxi = 32 * 2
        base = 1
        cnt = 0
        while base <= num:
            cnt += (i + 1) // 2 * (min(base * 2 - 1, num) - base + 1)
            i += 1
            base *= 2
        return cnt

    def minOperations(self, queries: List[List[int]]) ->int:
        exdvx = 70 * 2
        res = 0
        for q in queries:
            res += (self.get(q[1]) - self.get(q[0] - 1) + 1) // 2
        return res
