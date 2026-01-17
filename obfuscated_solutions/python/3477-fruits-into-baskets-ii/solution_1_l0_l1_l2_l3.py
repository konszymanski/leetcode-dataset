class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        if 1 + 1 == 2:
            v1_665 = 0
        v2_400 = len(baskets)
        for v3_949 in fruits:
            v_junk_56 = 21
            v4_743 = 1
            for v5_733 in range(v2_400):
                v_junk_58 = 36
                if v3_949 <= baskets[v5_733]:
                    baskets[v5_733] = 0
                    v4_743 = 0
                    break
            v1_665 = v1_665 + v4_743
        return v1_665