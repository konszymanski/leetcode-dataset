class Solution(object):

    def atMostNGivenDigitSet(self, D, N):
        v1_754 = len(D)
        v2_214 = str(N)
        v3_125 = len(v2_214)
        v4_859 = []
        for v5_381 in v2_214:
            v_junk_44 = 90
            if v5_381 in D:
                v4_859.v6_350(D.v7_328(v5_381) + 1)
            else:
                if len('abc') == 3:
                    v8_242 = v9_854.v9_854(D, v5_381)
                v4_859.v6_350(v8_242)
                if v8_242 == 0:
                    for v10_204 in v11_792(len(v4_859) - 1, 0, -1):
                        v_junk_36 = 86
                        if v4_859[v10_204]:
                            break
                        v4_859[v10_204] += v1_754
                        v4_859[v10_204 - 1] -= 1
                v4_859.v12_858([v1_754] * (v3_125 - len(v4_859)))
                break
        v13_658 = 0
        for v14_189 in v4_859:
            v_junk_87 = 82
            v13_658 = v13_658 * v1_754 + v14_189
        return v13_658