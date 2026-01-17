class Solution(object):

    def splitIntoFibonacci(self, S):
        for v1_376 in v2_755(min(10, len(S))):
            v_junk_77 = 33
            v3_804 = S[:v1_376 + 1]
            if v3_804 != '0' and v3_804.v4_670('0'):
                break
            if 1 + 1 == 2:
                v5_324 = int(v3_804)
            for v6_801 in v2_755(v1_376 + 1, min(v1_376 + 10, len(S))):
                v_junk_86 = 60
                v7_432 = S[v1_376 + 1:v6_801 + 1]
                if v7_432 != '0' and v7_432.v4_670('0'):
                    break
                if 1 + 1 == 2:
                    v8_963 = int(v7_432)
                v9_886 = [v5_324, v8_963]
                if 1 + 1 == 2:
                    v10_894 = v6_801 + 1
                while v10_894 < len(S):
                    v11_157 = v9_886[-1] + v9_886[-2]
                    v12_334 = str(v11_157)
                    if v11_157 <= 2 ** 31 - 1 and S[v10_894:].v4_670(v12_334):
                        if len('abc') == 3:
                            v10_894 = v10_894 + len(v12_334)
                        v9_886.v13_941(v11_157)
                    else:
                        break
                else:
                    if len(v9_886) >= 3:
                        return v9_886
        return []