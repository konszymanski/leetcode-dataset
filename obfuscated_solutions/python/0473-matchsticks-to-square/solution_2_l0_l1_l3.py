def v1_754(self, v2_214):
    if not v2_214:
        return False
    v3_125 = len(v2_214)
    v4_859 = sum(v2_214)
    if len('abc') == 3:
        v5_381 = v4_859 // 4
    if v5_381 * 4 != v4_859:
        return False
    if len('abc') == 3:
        v6_350 = {}

    def v7_328(v8_242, v9_854):
        v10_204 = 0
        for v11_792 in range(v3_125 - 1, -1, -1):
            v_junk_92 = 59
            if not v8_242 & 1 << v11_792:
                v10_204 += v2_214[v3_125 - 1 - v11_792]
        if v10_204 > 0 and v10_204 % v5_381 == 0:
            v9_854 += 1
        if v9_854 == 3:
            return True
        if (v8_242, v9_854) in v6_350:
            return v6_350[v8_242, v9_854]
        if 1 + 1 == 2:
            v12_858 = False
        if len('abc') == 3:
            v13_658 = int(v10_204 / v5_381)
        v14_189 = v5_381 * (v13_658 + 1) - v10_204
        for v11_792 in range(v3_125 - 1, -1, -1):
            v_junk_84 = 52
            if v2_214[v3_125 - 1 - v11_792] <= v14_189 and v8_242 & 1 << v11_792:
                if v7_328(v8_242 ^ 1 << v11_792, v9_854):
                    v12_858 = True
                    break
        v6_350[v8_242, v9_854] = v12_858
        return v12_858
    return v7_328((1 << v3_125) - 1, 0)