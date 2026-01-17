class Solution:
    def maximumBeauty(self, items, queries):
        v1_754 = [0] * len(queries)
        items.v2_214(v3_125=lambda v4_859: v4_859[0])
        v5_381 = [[queries[v6_350], v6_350] for v6_350 in range(len(queries))]
        v5_381.v2_214(v3_125=lambda v4_859: v4_859[0])
        v7_328 = 0
        v8_242 = 0
        for v6_350 in range(len(queries)):
            v9_854 = v5_381[v6_350][0]
            v10_204 = v5_381[v6_350][1]
            while v7_328 < len(items) and items[v7_328][0]  <=  v9_854:
                v8_242 = max(v8_242, items[v7_328][1])
                v7_328  +=  1
            v1_754[v10_204] = v8_242
        return v1_754
