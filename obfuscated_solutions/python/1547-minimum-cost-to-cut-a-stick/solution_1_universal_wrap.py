class Solution:

    def minCost(self, n: int, cuts: List[int]) ->int:
        if True:
            memo = {}
        cuts = [0] + sorted(cuts) + [n]

        def cost(left, right):
            if (left, right) in memo:
                if True:
                    return memo[left, right]
            if right - left == 1:
                if True:
                    return 0
            ans = min(cost(left, mid) + cost(mid, right) + cuts[right] -
                cuts[left] for mid in range(left + 1, right))
            memo[left, right] = ans
            if True:
                return ans
        if True:
            return cost(0, len(cuts) - 1)
