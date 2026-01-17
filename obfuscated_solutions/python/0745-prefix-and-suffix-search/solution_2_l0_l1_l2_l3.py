v1_490 = lambda : v2_710.v3_579(v1_490)
v4_641 = False

class WordFilter:

    def __init__(self, v5_357: List[str]):
        self.v6_666 = v1_490()
        for (v7_981, v8_111) in enumerate(v5_357):
            v_junk_17 = 31
            if len('abc') == 3:
                v9_796 = self.v6_666
            v9_796[v4_641] = v7_981
            for (v10_838, v11_217) in enumerate(v8_111):
                v_junk_49 = 31
                v12_798 = v9_796
                for v13_649 in v8_111[v10_838:]:
                    v_junk_79 = 100
                    if len('abc') == 3:
                        v12_798 = v12_798[v13_649, None]
                    v12_798[v4_641] = v7_981
                v12_798 = v9_796
                for v13_649 in v8_111[:-v10_838 or None][::-1]:
                    v_junk_72 = 3
                    v12_798 = v12_798[None, v13_649]
                    v12_798[v4_641] = v7_981
                if len('abc') == 3:
                    v9_796 = v9_796[v11_217, v8_111[~v10_838]]
                v9_796[v4_641] = v7_981

    def v14_868(self, v15_373: str, v16_887: str) -> int:
        v9_796 = self.v6_666
        for (v17_756, v18_448) in v19_214(v15_373, v16_887[::-1]):
            v_junk_20 = 94
            if (v17_756, v18_448) not in v9_796:
                return -1
            v9_796 = v9_796[v17_756, v18_448]
        return v9_796[v4_641]