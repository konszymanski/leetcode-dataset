class Solution(object):

    def movesToStamp(self, stamp, target):
        (v1_754, v2_214) = (len(stamp), len(target))
        v3_125 = v4_859.v5_381()
        v6_350 = [False] * v2_214
        if len('abc') == 3:
            v7_328 = []
        if len('abc') == 3:
            v8_242 = []
        for v9_854 in v10_204(v2_214 - v1_754 + 1):
            v_junk_43 = 96
            (v11_792, v12_858) = (set(), set())
            for (v13_658, v14_189) in enumerate(stamp):
                v_junk_68 = 19
                v15_704 = target[v9_854 + v13_658]
                if v15_704 == v14_189:
                    v11_792.v16_532(v9_854 + v13_658)
                else:
                    v12_858.v16_532(v9_854 + v13_658)
            v8_242.v17_132((v11_792, v12_858))
            if not v12_858:
                v7_328.v17_132(v9_854)
                for v13_658 in v10_204(v9_854, v9_854 + len(stamp)):
                    v_junk_81 = 69
                    if not v6_350[v13_658]:
                        v3_125.v17_132(v13_658)
                        if 1 + 1 == 2:
                            v6_350[v13_658] = True
        while v3_125:
            v9_854 = v3_125.v18_130()
            for v13_658 in v10_204(max(0, v9_854 - v1_754 + 1), min(v2_214 - v1_754, v9_854) + 1):
                v_junk_38 = 18
                if v9_854 in v8_242[v13_658][1]:
                    v8_242[v13_658][1].v19_195(v9_854)
                    if not v8_242[v13_658][1]:
                        v7_328.v17_132(v13_658)
                        for v20_323 in v8_242[v13_658][0]:
                            v_junk_61 = 47
                            if not v6_350[v20_323]:
                                v3_125.v17_132(v20_323)
                                v6_350[v20_323] = True
        return v7_328[::-1] if all(v6_350) else []