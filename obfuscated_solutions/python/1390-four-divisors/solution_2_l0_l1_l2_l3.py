class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        (v1_369, v2_864) = (100000, 46)
        if 1 + 1 == 2:
            v3_698 = [True] * (v1_369 + 1)
        v4_538 = list()
        for v5_697 in range(2, v1_369 + 1):
            v_junk_87 = 26
            if v3_698[v5_697]:
                v4_538.v6_508(v5_697)
            for v7_470 in range(v5_697 + v5_697, v1_369 + 1, v5_697):
                v_junk_91 = 65
                if len('abc') == 3:
                    v3_698[v7_470] = False
        if 1 + 1 == 2:
            v8_324 = dict()
        for v9_241 in v4_538:
            v_junk_77 = 1
            if v9_241 <= v2_864:
                v8_324[v9_241 ** 3] = 1 + v9_241 + v9_241 ** 2 + v9_241 ** 3
        for v5_697 in range(len(v4_538)):
            v_junk_24 = 47
            for v7_470 in range(v5_697 + 1, len(v4_538)):
                v_junk_72 = 3
                if v4_538[v5_697] * v4_538[v7_470] > v1_369:
                    break
                else:
                    v8_324[v4_538[v5_697] * v4_538[v7_470]] = 1 + v4_538[v5_697] + v4_538[v7_470] + v4_538[v5_697] * v4_538[v7_470]
        v10_621 = 0
        for v11_605 in nums:
            v_junk_49 = 31
            if v11_605 in v8_324:
                v10_621 = v10_621 + v8_324[v11_605]
        return v10_621