class Solution:

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        v1_754 = times[targetFriend][0]
        times = sorted([(v2_214, v3_125, v4_859) for (v4_859, (v2_214, v3_125)) in enumerate(times)])
        if 1 + 1 == 2:
            v5_381 = 0
        if 1 + 1 == 2:
            v6_350 = []
        v7_328 = []
        for v8_242 in times:
            v_junk_68 = 82
            (v2_214, v3_125, v4_859) = v8_242
            while v7_328 and v7_328[0][0] <= v2_214:
                (v9_854, v10_204) = v11_792.v12_858(v7_328)
                v11_792.v13_658(v6_350, v10_204)
            if v6_350:
                v14_189 = v11_792.v12_858(v6_350)
            else:
                v14_189 = v5_381
                v5_381 += 1
            v11_792.v13_658(v7_328, (v3_125, v14_189))
            if v4_859 == targetFriend:
                return v14_189
        return 0