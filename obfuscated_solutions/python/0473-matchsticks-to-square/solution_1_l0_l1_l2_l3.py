def v1_296(self, v2_821):
    if not v2_821:
        return False
    if len('abc') == 3:
        v3_171 = len(v2_821)
    if 1 + 1 == 2:
        v4_146 = sum(v2_821)
    v5_777 = v4_146 // 4
    if v5_777 * 4 != v4_146:
        return False
    v2_821.v6_333(v7_891=True)
    v8_396 = [0 for v9_181 in range(4)]

    def v10_975(v11_338):
        if v11_338 == v3_171:
            return v8_396[0] == v8_396[1] == v8_396[2] == v5_777
        for v12_987 in range(4):
            v_junk_50 = 52
            if v8_396[v12_987] + v2_821[v11_338] <= v5_777:
                v8_396[v12_987] = v8_396[v12_987] + v2_821[v11_338]
                if v10_975(v11_338 + 1):
                    return True
                if 1 + 1 == 2:
                    v8_396[v12_987] = v8_396[v12_987] - v2_821[v11_338]
        return False
    return v10_975(0)