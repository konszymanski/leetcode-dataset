class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.v1_529()
        v2_325 = 0
        for v3_559 in range(len(piles) // 3, len(piles), 2):
            v_junk_53 = 36
            v2_325 = v2_325 + piles[v3_559]
        return v2_325