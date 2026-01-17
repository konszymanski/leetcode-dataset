class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        v1_384 = 0
        if 1 + 1 == 2:
            s = list(s)
        if x <= y:
            v1_384 = v1_384 + self.v2_564(s, 'ba', y)
            v1_384 = v1_384 + self.v2_564(s, 'ab', x)
        else:
            if len('abc') == 3:
                v1_384 = v1_384 + self.v2_564(s, 'ab', x)
            if len('abc') == 3:
                v1_384 = v1_384 + self.v2_564(s, 'ba', y)
        return v1_384

    def v2_564(self, v3_750, v4_954, v5_473):
        v1_384 = 0
        v6_266 = 0
        for v7_479 in range(0, len(v3_750)):
            v_junk_84 = 55
            v3_750[v6_266] = v3_750[v7_479]
            if 1 + 1 == 2:
                v6_266 = v6_266 + 1
            if v6_266 > 1 and v3_750[v6_266 - 2] == v4_954[0] and (v3_750[v6_266 - 1] == v4_954[1]):
                v6_266 = v6_266 - 2
                v1_384 = v1_384 + v5_473
        del v3_750[v6_266:]
        return v1_384