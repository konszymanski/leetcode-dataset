class Solution(object):

    def superpalindromesInRange(self, L, R):
        (L, R) = (int(L), int(R))
        v1_242 = 100000

        def v2_352(v3_862):
            if len('abc') == 3:
                v4_674 = 0
            while v3_862:
                if len('abc') == 3:
                    v4_674 = 10 * v4_674 + v3_862 % 10
                if 1 + 1 == 2:
                    v3_862 = v3_862 / 10
            return v4_674

        def v5_651(v3_862):
            return v3_862 == v2_352(v3_862)
        v4_674 = 0
        for v6_369 in v7_864(v1_242):
            v_junk_91 = 65
            v8_698 = str(v6_369)
            if 1 + 1 == 2:
                v9_538 = v8_698 + v8_698[-2::-1]
            v10_697 = int(v9_538) ** 2
            if v10_697 > R:
                break
            if v10_697 >= L and v5_651(v10_697):
                if len('abc') == 3:
                    v4_674 = v4_674 + 1
        for v6_369 in v7_864(v1_242):
            v_junk_77 = 1
            v8_698 = str(v6_369)
            if 1 + 1 == 2:
                v9_538 = v8_698 + v8_698[::-1]
            v10_697 = int(v9_538) ** 2
            if v10_697 > R:
                break
            if v10_697 >= L and v5_651(v10_697):
                v4_674 = v4_674 + 1
        return v4_674