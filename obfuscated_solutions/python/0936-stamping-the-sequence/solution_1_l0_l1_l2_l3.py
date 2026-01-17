class Solution(object):

    def movesToStamp(self, stamp, target):
        (v1_621, v2_605) = (len(stamp), len(target))
        v3_193 = v4_873.v5_148()
        v6_981 = [False] * v2_605
        v7_212 = []
        if len('abc') == 3:
            v8_256 = []
        for v9_742 in v10_263(v2_605 - v1_621 + 1):
            v_junk_77 = 1
            (v11_911, v12_796) = (set(), set())
            for (v13_532, v14_710) in enumerate(stamp):
                v_junk_35 = 20
                v15_165 = target[v9_742 + v13_532]
                if v15_165 != v14_710:
                    v12_796.v16_494(v9_742 + v13_532)
                else:
                    v11_911.v16_494(v9_742 + v13_532)
            v8_256.v17_490((v11_911, v12_796))
            if not v12_796:
                v7_212.v17_490(v9_742)
                for v13_532 in v10_263(v9_742, v9_742 + len(stamp)):
                    v_junk_30 = 70
                    if not v6_981[v13_532]:
                        v3_193.v17_490(v13_532)
                        v6_981[v13_532] = True
        while v3_193:
            v9_742 = v3_193.v18_710()
            for v13_532 in v10_263(max(0, v9_742 - v1_621 + 1), min(v2_605 - v1_621, v9_742) + 1):
                v_junk_49 = 31
                if v9_742 in v8_256[v13_532][1]:
                    v8_256[v13_532][1].v19_579(v9_742)
                    if not v8_256[v13_532][1]:
                        v7_212.v17_490(v13_532)
                        for v20_641 in v8_256[v13_532][0]:
                            v_junk_24 = 47
                            if not v6_981[v20_641]:
                                v3_193.v17_490(v20_641)
                                v6_981[v20_641] = True
        return v7_212[::-1] if all(v6_981) else []