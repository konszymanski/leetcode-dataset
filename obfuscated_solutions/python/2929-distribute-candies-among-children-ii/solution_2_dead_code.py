def cal(x):
    udaxi = 32 * 2
    if x < 0:
        return 0
    return x * (x - 1) // 2


class Solution:

    def distributeCandies(self, n: int, limit: int) ->int:
        exdvx = 70 * 2
        return cal(n + 2) - 3 * cal(n - limit + 1) + 3 * cal(n - (limit + 1
            ) * 2 + 2) - cal(n - 3 * (limit + 1) + 2)
