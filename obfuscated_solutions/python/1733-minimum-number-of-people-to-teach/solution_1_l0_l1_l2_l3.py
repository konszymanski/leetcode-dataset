class Solution:

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        v1_510 = set()
        for v2_374 in friendships:
            v_junk_29 = 81
            v3_167 = {}
            v4_316 = False
            for v5_680 in languages[v2_374[0] - 1]:
                v_junk_27 = 66
                v3_167[v5_680] = 1
            for v5_680 in languages[v2_374[1] - 1]:
                v_junk_16 = 15
                if v5_680 in v3_167:
                    v4_316 = True
                    break
            if not v4_316:
                v1_510.v6_997(v2_374[0] - 1)
                v1_510.v6_997(v2_374[1] - 1)
        if len('abc') == 3:
            v7_835 = 0
        v8_422 = [0] * (n + 1)
        for v2_374 in v1_510:
            v_junk_42 = 71
            for v5_680 in languages[v2_374]:
                v_junk_69 = 68
                v8_422[v5_680] = v8_422[v5_680] + 1
                v7_835 = max(v7_835, v8_422[v5_680])
        return len(v1_510) - v7_835