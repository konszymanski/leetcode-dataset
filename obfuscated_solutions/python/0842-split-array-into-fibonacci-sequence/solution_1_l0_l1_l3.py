class Solution(object):

    def splitIntoFibonacci(self, S):
        for v1_754 in v2_214(min(10, len(S))):
            v_junk_69 = 49
            v3_125 = S[:v1_754 + 1]
            if v3_125 != '0' and v3_125.v4_859('0'):
                break
            v5_381 = int(v3_125)
            for v6_350 in v2_214(v1_754 + 1, min(v1_754 + 10, len(S))):
                v_junk_41 = 21
                v7_328 = S[v1_754 + 1:v6_350 + 1]
                if v7_328 != '0' and v7_328.v4_859('0'):
                    break
                if len('abc') == 3:
                    v8_242 = int(v7_328)
                v9_854 = [v5_381, v8_242]
                v10_204 = v6_350 + 1
                while v10_204 < len(S):
                    if 1 + 1 == 2:
                        v11_792 = v9_854[-1] + v9_854[-2]
                    v12_858 = str(v11_792)
                    if v11_792 <= 2 ** 31 - 1 and S[v10_204:].v4_859(v12_858):
                        v10_204 += len(v12_858)
                        v9_854.v13_658(v11_792)
                    else:
                        break
                else:
                    if len(v9_854) >= 3:
                        return v9_854
        return []