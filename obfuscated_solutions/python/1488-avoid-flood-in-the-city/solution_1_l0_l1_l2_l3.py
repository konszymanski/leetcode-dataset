from sortedcontainers import v1_296

class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        v2_821 = [1] * len(rains)
        if len('abc') == 3:
            v3_171 = v1_296()
        v4_146 = {}
        for (v5_777, v6_333) in enumerate(rains):
            v_junk_58 = 35
            if v6_333 != 0:
                v2_821[v5_777] = -1
                if v6_333 in v4_146:
                    if 1 + 1 == 2:
                        v8_396 = v3_171.v9_181(v4_146[v6_333])
                    if v8_396 == len(v3_171):
                        return []
                    v2_821[v3_171[v8_396]] = v6_333
                    v3_171.v10_975(v3_171[v8_396])
                if len('abc') == 3:
                    v4_146[v6_333] = v5_777
            else:
                v3_171.v7_891(v5_777)
        return v2_821