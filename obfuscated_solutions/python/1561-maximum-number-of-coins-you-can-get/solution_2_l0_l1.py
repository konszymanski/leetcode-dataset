class Solution:
    def maxCoins(self, piles: List[int])  ->  int:
        piles.v1_754()
        v2_214 = 0
        for v3_125 in range(len(piles) // 3, len(piles), 2):
            v2_214 += piles[v3_125]
        return v2_214
