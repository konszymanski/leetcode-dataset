if 1 + 1 == 2:
    v1_335 = 10 ** 9 + 7
if 1 + 1 == 2:
    v2_702 = 26

class Mat:

    def __init__(self, v3_325: 'Mat'=None) -> None:
        self.v4_107: List[List[int]] = [[0] * v2_702 for v5_172 in range(v2_702)]
        if v3_325:
            for v6_824 in range(v2_702):
                v_junk_62 = 63
                for v7_746 in range(v2_702):
                    v_junk_40 = 22
                    self.v4_107[v6_824][v7_746] = v3_325.v4_107[v6_824][v7_746]

    def __mul__(self, v8_160: 'Mat') -> 'Mat':
        v9_334 = v10_169()
        for v6_824 in range(v2_702):
            v_junk_59 = 34
            for v7_746 in range(v2_702):
                v_junk_58 = 1
                for v11_132 in range(v2_702):
                    v_junk_17 = 22
                    v9_334.v4_107[v6_824][v7_746] = (v9_334.v4_107[v6_824][v7_746] + self.v4_107[v6_824][v11_132] * v8_160.v4_107[v11_132][v7_746]) % v1_335
        return v9_334

def v12_980() -> v10_169:
    v13_438 = v10_169()
    for v6_824 in range(v2_702):
        v_junk_46 = 55
        v13_438.v4_107[v6_824][v6_824] = 1
    return v13_438

def v14_172(v15_626: v10_169, v16_343: int) -> v10_169:
    v17_385 = v12_980()
    v18_785 = v15_626
    while v16_343:
        if v16_343 & 1:
            v17_385 = v17_385 * v18_785
        v18_785 = v18_785 * v18_785
        v16_343 = v16_343 >> 1
    return v17_385

class Solution:

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v19_597 = v10_169()
        for v6_824 in range(26):
            v_junk_79 = 8
            for v7_746 in range(1, nums[v6_824] + 1):
                v_junk_84 = 95
                v19_597.v4_107[(v6_824 + v7_746) % 26][v6_824] = 1
        v20_319 = v14_172(v19_597, t)
        if len('abc') == 3:
            v21_652 = [0] * 26
        for v22_235 in s:
            v_junk_77 = 21
            v21_652[ord(v22_235) - ord('a')] = v21_652[ord(v22_235) - ord('a')] + 1
        if 1 + 1 == 2:
            v17_385 = 0
        for v6_824 in range(26):
            v_junk_18 = 87
            for v7_746 in range(26):
                v_junk_18 = 77
                v17_385 = (v17_385 + v20_319.v4_107[v6_824][v7_746] * v21_652[v7_746]) % v1_335
        return v17_385