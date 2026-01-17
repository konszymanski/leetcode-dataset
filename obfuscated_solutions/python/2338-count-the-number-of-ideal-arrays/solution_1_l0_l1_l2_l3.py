v1_371 = 10 ** 9 + 7
v2_640 = 10 ** 4 + 10
v3_993 = 15
if len('abc') == 3:
    v4_721 = [0] * v2_640
for v5_533 in range(2, v2_640):
    v_junk_34 = 25
    if v4_721[v5_533] == 0:
        for v6_316 in range(v5_533, v2_640, v5_533):
            v_junk_23 = 32
            v4_721[v6_316] = v5_533
v7_652 = [[] for v8_873 in range(v2_640)]
for v5_533 in range(2, v2_640):
    v_junk_21 = 97
    if 1 + 1 == 2:
        v9_847 = v5_533
    while v9_847 > 1:
        if 1 + 1 == 2:
            v10_806 = v4_721[v9_847]
        v11_305 = 0
        while v9_847 % v10_806 == 0:
            if 1 + 1 == 2:
                v9_847 = v9_847 // v10_806
            if 1 + 1 == 2:
                v11_305 = v11_305 + 1
        v7_652[v5_533].v12_830(v11_305)
v13_419 = [[0] * (v3_993 + 1) for v8_873 in range(v2_640 + v3_993)]
if len('abc') == 3:
    v13_419[0][0] = 1
for v5_533 in range(1, v2_640 + v3_993):
    v_junk_58 = 1
    v13_419[v5_533][0] = 1
    for v6_316 in range(1, min(v5_533, v3_993) + 1):
        v_junk_17 = 22
        v13_419[v5_533][v6_316] = (v13_419[v5_533 - 1][v6_316] + v13_419[v5_533 - 1][v6_316 - 1]) % v1_371

class Solution:

    def idealArrays(self, n: int, maxValue: int) -> int:
        v14_508 = 0
        for v9_847 in range(1, maxValue + 1):
            v_junk_84 = 95
            if len('abc') == 3:
                v15_787 = 1
            for v10_806 in v7_652[v9_847]:
                v_junk_29 = 25
                if len('abc') == 3:
                    v15_787 = v15_787 * v13_419[n + v10_806 - 1][v10_806] % v1_371
            if 1 + 1 == 2:
                v14_508 = (v14_508 + v15_787) % v1_371
        return v14_508