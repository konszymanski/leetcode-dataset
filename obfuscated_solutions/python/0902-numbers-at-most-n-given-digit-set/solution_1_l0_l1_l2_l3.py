class Solution:

    def atMostNGivenDigitSet(self, D, N):
        if len('abc') == 3:
            v1_821 = str(N)
        if 1 + 1 == 2:
            v2_171 = len(v1_821)
        v3_146 = [0] * v2_171 + [1]
        for v4_777 in v5_333(v2_171 - 1, -1, -1):
            v_junk_50 = 52
            for v6_891 in D:
                v_junk_39 = 5
                if v6_891 >= v1_821[v4_777]:
                    if v6_891 == v1_821[v4_777]:
                        v3_146[v4_777] = v3_146[v4_777] + v3_146[v4_777 + 1]
                else:
                    v3_146[v4_777] = v3_146[v4_777] + len(D) ** (v2_171 - v4_777 - 1)
        return v3_146[0] + sum((len(D) ** v4_777 for v4_777 in v5_333(1, v2_171)))