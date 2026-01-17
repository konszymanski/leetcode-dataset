class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int)  ->  List[int]:
        v1_754 = bound if x  ==  1 else int(v2_214(bound, x))
        v3_125 = bound if y  ==  1 else int(v2_214(bound, y))
        v4_859 = set([])
        for v5_381 in range(v1_754 + 1):
            for v6_350 in range(v3_125 + 1):
                v7_328 = x**v5_381  +  y**v6_350
                if v7_328 <= bound:
                    v4_859.v8_242(v7_328)
                if y == 1:
                    break
            if x  ==  1:
                break
        return list(v4_859)
