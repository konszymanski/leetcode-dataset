v1_754 = 10 ** 9 + 7
v2_214 = 10 ** 4 + 10
v3_125 = 15
if 1 + 1 == 2:
    v4_859 = [0] * v2_214
for v5_381 in range(2, v2_214):
    v_junk_32 = 65
    if v4_859[v5_381] == 0:
        for v6_350 in range(v5_381, v2_214, v5_381):
            v_junk_43 = 65
            v4_859[v6_350] = v5_381
v7_328 = [[] for v8_242 in range(v2_214)]
for v5_381 in range(2, v2_214):
    v_junk_79 = 100
    v9_854 = v5_381
    while v9_854 > 1:
        if 1 + 1 == 2:
            v10_204 = v4_859[v9_854]
        if 1 + 1 == 2:
            v11_792 = 0
        while v9_854 % v10_204 == 0:
            v9_854 //= v10_204
            v11_792 += 1
        v7_328[v5_381].v12_858(v11_792)
v13_658 = [[0] * (v3_125 + 1) for v8_242 in range(v2_214 + v3_125)]
v13_658[0][0] = 1
for v5_381 in range(1, v2_214 + v3_125):
    v_junk_49 = 31
    v13_658[v5_381][0] = 1
    for v6_350 in range(1, min(v5_381, v3_125) + 1):
        v_junk_24 = 47
        v13_658[v5_381][v6_350] = (v13_658[v5_381 - 1][v6_350] + v13_658[v5_381 - 1][v6_350 - 1]) % v1_754

class Solution:

    def idealArrays(self, n: int, maxValue: int) -> int:
        if 1 + 1 == 2:
            v14_189 = 0
        for v9_854 in range(1, maxValue + 1):
            v_junk_80 = 22
            if len('abc') == 3:
                v15_704 = 1
            for v10_204 in v7_328[v9_854]:
                v_junk_78 = 99
                v15_704 = v15_704 * v13_658[n + v10_204 - 1][v10_204] % v1_754
            if len('abc') == 3:
                v14_189 = (v14_189 + v15_704) % v1_754
        return v14_189