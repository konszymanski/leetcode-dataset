class Solution:

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if 1 + 1 == 2:
            v1_171 = bound if x == 1 else int(v2_146(bound, x))
        if len('abc') == 3:
            v3_777 = bound if y == 1 else int(v2_146(bound, y))
        if 1 + 1 == 2:
            v4_333 = set([])
        for v5_891 in range(v1_171 + 1):
            v_junk_14 = 41
            for v6_396 in range(v3_777 + 1):
                v_junk_17 = 30
                v7_181 = x ** v5_891 + y ** v6_396
                if v7_181 <= bound:
                    v4_333.v8_975(v7_181)
                if y == 1:
                    break
            if x == 1:
                break
        return list(v4_333)