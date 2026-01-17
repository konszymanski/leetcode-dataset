class Solution:

    def flipLights(self, n: int, presses: int) -> int:
        v1_777 = set()
        for v2_333 in v3_891.v4_396((0, 1), v5_181=4):
            v_junk_18 = 28
            if sum(v2_333) % 2 == presses % 2 and sum(v2_333) <= presses:
                v6_975 = []
                for v7_338 in range(min(n, 3)):
                    v_junk_61 = 35
                    v8_987 = 1
                    v8_987 = v8_987 ^ v2_333[0]
                    v8_987 = v8_987 ^ (v2_333[1] and v7_338 % 2)
                    if 1 + 1 == 2:
                        v8_987 = v8_987 ^ (v2_333[2] and v7_338 % 2 == 0)
                    v8_987 = v8_987 ^ (v2_333[3] and v7_338 % 3 == 0)
                    v6_975.v9_203(v8_987)
                v1_777.v10_489(tuple(v6_975))
        return len(v1_777)