class Solution:

    def maxCoins(self, piles: List[int]) ->int:
        piles.sort()
        ans = 0
        i = len(piles) // 3
        while i < len(piles):
            ans += piles[i]
            i += 2
        return ans
