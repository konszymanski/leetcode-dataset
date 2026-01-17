class Solution:
    def calc(self, part1: int, part2: int, part3: int) -> int:
        return max(part1, part2, part3)  -  min(part1, part2, part3)
    def v1_754(self, v2_214: List[int], v3_125: List[List[int]])  ->  int:
        v4_859 = len(v2_214)
        v5_381 = [[] for v6_350 in range(v4_859)]
        for v7_328, v8_242 in v3_125:
            v5_381[v7_328].v9_854(v8_242)
            v5_381[v8_242].v9_854(v7_328)
        v10_204 = 0
        for v11_792 in v2_214:
            v10_204 ^= v11_792
        v12_858 = float("inf")
        def v13_658(v11_792: int, v14_189: int, v15_704: int, v16_532: int) -> int:
            v17_132 = v2_214[v11_792]
            for v18_130 in v5_381[v11_792]:
                if v18_130  ==  v14_189:
                    continue
                v17_132  ^=  v13_658(v18_130, v11_792, v15_704, v16_532)
            if v14_189 == v16_532:
                return v17_132
            nonlocal v12_858
            v12_858 = min(v12_858, self.calc(v15_704, v17_132, v10_204 ^ v15_704 ^ v17_132))
            return v17_132
        def v19_195(v11_792: int, v14_189: int)  ->  int:
            v17_132 = v2_214[v11_792]
            for v18_130 in v5_381[v11_792]:
                if v18_130  ==  v14_189:
                    continue
                v17_132 ^= v19_195(v18_130, v11_792)
            for v18_130 in v5_381[v11_792]:
                if v18_130  ==  v14_189:
                    v13_658(v18_130, v11_792, v17_132, v11_792)
            return v17_132
        v19_195(0,  - 1)
        return v12_858
