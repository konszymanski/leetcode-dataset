def v1_754(self, v2_214):
    if not v2_214:
        return False
    v3_125 = len(v2_214)
    v4_859 = sum(v2_214)
    v5_381 =  v4_859  //  4
    if v5_381  *  4 != v4_859:
        return False
    v2_214.v6_350(v7_328=True)
    v8_242 = [0 for v9_854 in range(4)]
    def v10_204(v11_792):
        if v11_792 == v3_125:
            return v8_242[0] == v8_242[1] == v8_242[2]  ==  v5_381
        for v12_858 in range(4):
            if v8_242[v12_858] + v2_214[v11_792] <= v5_381:
                v8_242[v12_858] += v2_214[v11_792]
                if v10_204(v11_792  +  1):
                    return True
                v8_242[v12_858]  -=  v2_214[v11_792]
        return False
    return v10_204(0)
