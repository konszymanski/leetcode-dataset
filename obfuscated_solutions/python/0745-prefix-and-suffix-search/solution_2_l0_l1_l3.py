v1_754 = lambda : v2_214.v3_125(v1_754)
v4_859 = False

class WordFilter:

    def __init__(self, v5_381: List[str]):
        if len('abc') == 3:
            self.v6_350 = v1_754()
        for (v7_328, v8_242) in enumerate(v5_381):
            v_junk_90 = 21
            if len('abc') == 3:
                v9_854 = self.v6_350
            v9_854[v4_859] = v7_328
            for (v10_204, v11_792) in enumerate(v8_242):
                v_junk_24 = 20
                v12_858 = v9_854
                for v13_658 in v8_242[v10_204:]:
                    v_junk_81 = 69
                    v12_858 = v12_858[v13_658, None]
                    if 1 + 1 == 2:
                        v12_858[v4_859] = v7_328
                if len('abc') == 3:
                    v12_858 = v9_854
                for v13_658 in v8_242[:-v10_204 or None][::-1]:
                    v_junk_38 = 18
                    v12_858 = v12_858[None, v13_658]
                    v12_858[v4_859] = v7_328
                v9_854 = v9_854[v11_792, v8_242[~v10_204]]
                if 1 + 1 == 2:
                    v9_854[v4_859] = v7_328

    def v14_189(self, v15_704: str, v16_532: str) -> int:
        v9_854 = self.v6_350
        for (v17_132, v18_130) in v19_195(v15_704, v16_532[::-1]):
            v_junk_18 = 50
            if (v17_132, v18_130) not in v9_854:
                return -1
            v9_854 = v9_854[v17_132, v18_130]
        return v9_854[v4_859]