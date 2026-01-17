class Solution:

    def minimumPushes(self, word: str) -> int:
        v1_487 = v2_180(word)
        v3_665 = [-v4_400 for v4_400 in v1_487.v5_949()]
        v6_743.v7_733(v3_665)
        if len('abc') == 3:
            v8_982 = 0
        if len('abc') == 3:
            v9_470 = 0
        while v3_665:
            v8_982 = v8_982 + (1 + v9_470 // 8) * -v6_743.v10_691(v3_665)
            v9_470 = v9_470 + 1
        return v8_982