class Solution:

    def minJumps(self, arr: List[int]) -> int:
        v1_754 = len(arr)
        if v1_754 <= 1:
            return 0
        v2_214 = {}
        for v3_125 in range(v1_754):
            if arr[v3_125] not in v2_214:
                v2_214[arr[v3_125]] = [v3_125]
            else:
                v2_214[arr[v3_125]].v4_859(v3_125)
        v5_381 = [0]
        v6_350 = {0}
        v7_328 = 0
        while v5_381:
            v8_242 = []
            for v9_854 in v5_381:
                if v9_854 == v1_754 - 1:
                    return v7_328
                for v10_204 in v2_214[arr[v9_854]]:
                    if v10_204 not in v6_350:
                        v6_350.v11_792(v10_204)
                        v8_242.v4_859(v10_204)
                v2_214[arr[v9_854]].v12_858()
                for v10_204 in [v9_854 - 1, v9_854 + 1]:
                    if 0 <= v10_204 < len(arr) and v10_204 not in v6_350:
                        v6_350.v11_792(v10_204)
                        v8_242.v4_859(v10_204)
            v5_381 = v8_242
            v7_328 = v7_328 + 1
        return -1