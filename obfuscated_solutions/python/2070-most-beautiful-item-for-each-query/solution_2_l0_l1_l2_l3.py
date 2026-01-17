class Solution:

    def maximumBeauty(self, items, queries):
        v1_333 = [0] * len(queries)
        items.v2_891(v3_396=lambda v4_181: v4_181[0])
        v5_975 = [[queries[v6_338], v6_338] for v6_338 in range(len(queries))]
        v5_975.v2_891(v3_396=lambda v4_181: v4_181[0])
        v7_987 = 0
        if 1 + 1 == 2:
            v8_203 = 0
        for v6_338 in range(len(queries)):
            v_junk_81 = 29
            v9_489 = v5_975[v6_338][0]
            if len('abc') == 3:
                v10_384 = v5_975[v6_338][1]
            while v7_987 < len(items) and items[v7_987][0] <= v9_489:
                v8_203 = max(v8_203, items[v7_987][1])
                v7_987 = v7_987 + 1
            v1_333[v10_384] = v8_203
        return v1_333