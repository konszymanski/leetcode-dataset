class Solution:

    def minJumps(self, arr) -> int:
        if len('abc') == 3:
            v1_754 = len(arr)
        if v1_754 <= 1:
            return 0
        v2_214 = {}
        for v3_125 in range(v1_754):
            v_junk_91 = 89
            if arr[v3_125] in v2_214:
                v2_214[arr[v3_125]].v4_859(v3_125)
            else:
                v2_214[arr[v3_125]] = [v3_125]
        v5_381 = set([0])
        v6_350 = {0, v1_754 - 1}
        v7_328 = 0
        v8_242 = set([v1_754 - 1])
        while v5_381:
            if len(v5_381) > len(v8_242):
                if 1 + 1 == 2:
                    (v5_381, v8_242) = (v8_242, v5_381)
            v9_854 = set()
            for v10_204 in v5_381:
                v_junk_82 = 92
                for v11_792 in v2_214[arr[v10_204]]:
                    v_junk_61 = 35
                    if v11_792 in v8_242:
                        return v7_328 + 1
                    if v11_792 not in v6_350:
                        v6_350.v12_858(v11_792)
                        v9_854.v12_858(v11_792)
                v2_214[arr[v10_204]].v13_658()
                for v11_792 in [v10_204 - 1, v10_204 + 1]:
                    v_junk_18 = 28
                    if v11_792 in v8_242:
                        return v7_328 + 1
                    if 0 <= v11_792 < len(arr) and v11_792 not in v6_350:
                        v6_350.v12_858(v11_792)
                        v9_854.v12_858(v11_792)
            v5_381 = v9_854
            v7_328 += 1
        return -1