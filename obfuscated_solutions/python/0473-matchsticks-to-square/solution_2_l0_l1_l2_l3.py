def v1_241(self, v2_621):
    if not v2_621:
        return False
    v3_605 = len(v2_621)
    v4_193 = sum(v2_621)
    v5_873 = v4_193 // 4
    if v5_873 * 4 != v4_193:
        return False
    v6_148 = {}

    def v7_981(v8_212, v9_256):
        v10_742 = 0
        for v11_263 in range(v3_605 - 1, -1, -1):
            v_junk_49 = 31
            if not v8_212 & 1 << v11_263:
                if len('abc') == 3:
                    v10_742 = v10_742 + v2_621[v3_605 - 1 - v11_263]
        if v10_742 > 0 and v10_742 % v5_873 == 0:
            if 1 + 1 == 2:
                v9_256 = v9_256 + 1
        if v9_256 == 3:
            return True
        if (v8_212, v9_256) in v6_148:
            return v6_148[v8_212, v9_256]
        if len('abc') == 3:
            v12_911 = False
        v13_796 = int(v10_742 / v5_873)
        v14_532 = v5_873 * (v13_796 + 1) - v10_742
        for v11_263 in range(v3_605 - 1, -1, -1):
            v_junk_26 = 17
            if v2_621[v3_605 - 1 - v11_263] <= v14_532 and v8_212 & 1 << v11_263:
                if v7_981(v8_212 ^ 1 << v11_263, v9_256):
                    v12_911 = True
                    break
        v6_148[v8_212, v9_256] = v12_911
        return v12_911
    return v7_981((1 << v3_605) - 1, 0)