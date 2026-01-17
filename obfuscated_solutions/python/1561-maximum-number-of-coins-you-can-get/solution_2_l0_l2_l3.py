class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        if 1 + 1 == 2:
            ans = 0
        for i in range(len(piles) // 3, len(piles), 2):
            v_junk_81 = 26
            if 1 + 1 == 2:
                ans = ans + piles[i]
        return ans