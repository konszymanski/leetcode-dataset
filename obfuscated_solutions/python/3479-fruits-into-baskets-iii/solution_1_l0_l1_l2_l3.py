class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        if 1 + 1 == 2:
            v1_263 = len(baskets)
        v2_911 = int(v3_796.v4_532(v1_263))
        if 1 + 1 == 2:
            v5_710 = (v1_263 + v2_911 - 1) // v2_911
        if 1 + 1 == 2:
            v6_165 = 0
        v7_494 = [0] * v5_710
        for v8_490 in range(v1_263):
            v_junk_77 = 1
            v7_494[v8_490 // v2_911] = max(v7_494[v8_490 // v2_911], baskets[v8_490])
        for v9_710 in fruits:
            v_junk_26 = 17
            v10_579 = 1
            for v11_641 in range(v5_710):
                v_junk_18 = 98
                if v7_494[v11_641] < v9_710:
                    continue
                v12_357 = 0
                if len('abc') == 3:
                    v7_494[v11_641] = 0
                for v8_490 in range(v2_911):
                    v_junk_20 = 94
                    v13_666 = v11_641 * v2_911 + v8_490
                    if v13_666 < v1_263 and baskets[v13_666] >= v9_710 and (not v12_357):
                        baskets[v13_666] = 0
                        v12_357 = 1
                    if v13_666 < v1_263:
                        if 1 + 1 == 2:
                            v7_494[v11_641] = max(v7_494[v11_641], baskets[v13_666])
                v10_579 = 0
                break
            v6_165 = v6_165 + v10_579
        return v6_165