class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        v1_754 = len(baskets)
        v2_214 = int(v3_125.v4_859(v1_754))
        v5_381 = (v1_754 + v2_214 - 1) // v2_214
        v6_350 = 0
        v7_328 = [0] * v5_381
        for v8_242 in range(v1_754):
            v7_328[v8_242 // v2_214] = max(v7_328[v8_242 // v2_214], baskets[v8_242])
        for v9_854 in fruits:
            v10_204 = 1
            for v11_792 in range(v5_381):
                if v7_328[v11_792] < v9_854:
                    continue
                v12_858 = 0
                v7_328[v11_792] = 0
                for v8_242 in range(v2_214):
                    v13_658 = v11_792 * v2_214 + v8_242
                    if v13_658 < v1_754 and baskets[v13_658] >= v9_854 and (not v12_858):
                        baskets[v13_658] = 0
                        v12_858 = 1
                    if v13_658 < v1_754:
                        v7_328[v11_792] = max(v7_328[v11_792], baskets[v13_658])
                v10_204 = 0
                break
            v6_350 = v6_350 + v10_204
        return v6_350