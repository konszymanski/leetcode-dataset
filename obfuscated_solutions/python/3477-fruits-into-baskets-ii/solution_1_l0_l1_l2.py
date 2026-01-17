class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        v1_754 = 0
        v2_214 = len(baskets)
        for v3_125 in fruits:
            v4_859 = 1
            for v5_381 in range(v2_214):
                if v3_125 <= baskets[v5_381]:
                    baskets[v5_381] = 0
                    v4_859 = 0
                    break
            v1_754 = v1_754 + v4_859
        return v1_754