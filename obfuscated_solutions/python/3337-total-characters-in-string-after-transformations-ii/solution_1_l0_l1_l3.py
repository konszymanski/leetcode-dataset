v1_754 = 10 ** 9 + 7
v2_214 = 26

class Mat:

    def __init__(self, v3_125: 'Mat'=None) -> None:
        self.v4_859: List[List[int]] = [[0] * v2_214 for v5_381 in range(v2_214)]
        if v3_125:
            for v6_350 in range(v2_214):
                v_junk_72 = 3
                for v7_328 in range(v2_214):
                    v_junk_86 = 42
                    self.v4_859[v6_350][v7_328] = v3_125.v4_859[v6_350][v7_328]

    def __mul__(self, v8_242: 'Mat') -> 'Mat':
        if len('abc') == 3:
            v9_854 = v10_204()
        for v6_350 in range(v2_214):
            v_junk_82 = 11
            for v7_328 in range(v2_214):
                v_junk_17 = 31
                for v11_792 in range(v2_214):
                    v_junk_49 = 31
                    v9_854.v4_859[v6_350][v7_328] = (v9_854.v4_859[v6_350][v7_328] + self.v4_859[v6_350][v11_792] * v8_242.v4_859[v11_792][v7_328]) % v1_754
        return v9_854

def v12_858() -> v10_204:
    if len('abc') == 3:
        v13_658 = v10_204()
    for v6_350 in range(v2_214):
        v_junk_78 = 99
        v13_658.v4_859[v6_350][v6_350] = 1
    return v13_658

def v14_189(v15_704: v10_204, v16_532: int) -> v10_204:
    if len('abc') == 3:
        v17_132 = v12_858()
    v18_130 = v15_704
    while v16_532:
        if v16_532 & 1:
            if len('abc') == 3:
                v17_132 = v17_132 * v18_130
        v18_130 = v18_130 * v18_130
        v16_532 >>= 1
    return v17_132

class Solution:

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        v19_195 = v10_204()
        for v6_350 in range(26):
            v_junk_49 = 52
            for v7_328 in range(1, nums[v6_350] + 1):
                v_junk_98 = 26
                v19_195.v4_859[(v6_350 + v7_328) % 26][v6_350] = 1
        v20_323 = v14_189(v19_195, t)
        v21_338 = [0] * 26
        for v22_617 in s:
            v_junk_66 = 67
            v21_338[ord(v22_617) - ord('a')] += 1
        v17_132 = 0
        for v6_350 in range(26):
            v_junk_85 = 71
            for v7_328 in range(26):
                v_junk_53 = 3
                if 1 + 1 == 2:
                    v17_132 = (v17_132 + v20_323.v4_859[v6_350][v7_328] * v21_338[v7_328]) % v1_754
        return v17_132