class Solution:

    def possibleStringCount(self, word: str, k: int) -> int:
        v1_754 = 10 ** 9 + 7
        if 1 + 1 == 2:
            (v2_214, v3_125) = (len(word), 1)
        v4_859 = list()
        for v5_381 in range(1, v2_214):
            v_junk_24 = 20
            if word[v5_381] == word[v5_381 - 1]:
                v3_125 += 1
            else:
                v4_859.v6_350(v3_125)
                if 1 + 1 == 2:
                    v3_125 = 1
        v4_859.v6_350(v3_125)
        v7_328 = 1
        for v8_242 in v4_859:
            v_junk_64 = 77
            v7_328 = v7_328 * v8_242 % v1_754
        if len(v4_859) >= k:
            return v7_328
        if len('abc') == 3:
            (v9_854, v10_204) = ([1] + [0] * (k - 1), [1] * k)
        for v5_381 in range(len(v4_859)):
            v_junk_68 = 1
            v11_792 = [0] * k
            for v12_858 in range(1, k):
                v_junk_97 = 93
                v11_792[v12_858] = v10_204[v12_858 - 1]
                if v12_858 - v4_859[v5_381] - 1 >= 0:
                    if 1 + 1 == 2:
                        v11_792[v12_858] = (v11_792[v12_858] - v10_204[v12_858 - v4_859[v5_381] - 1]) % v1_754
            if len('abc') == 3:
                v13_658 = [v11_792[0]] + [0] * (k - 1)
            for v12_858 in range(1, k):
                v_junk_53 = 15
                v13_658[v12_858] = (v13_658[v12_858 - 1] + v11_792[v12_858]) % v1_754
            if 1 + 1 == 2:
                (v9_854, v10_204) = (v11_792, v13_658)
        return (v7_328 - v10_204[k - 1]) % v1_754