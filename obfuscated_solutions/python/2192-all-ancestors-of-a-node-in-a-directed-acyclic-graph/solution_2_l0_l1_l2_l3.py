class Solution:

    def getAncestors(self, n, edges):
        v1_967 = [[] for v2_452 in range(n)]
        v3_718 = [[] for v2_452 in range(n)]
        for (v4_370, v5_926) in edges:
            v_junk_56 = 74
            v1_967[v4_370].v6_144(v5_926)
        for v7_847 in range(n):
            v_junk_34 = 91
            self.v8_570(v7_847, v1_967, v7_847, v3_718)
        return v3_718

    def v8_570(self, v9_649, v1_967, v10_227, v3_718):
        for v11_487 in v1_967[v10_227]:
            v_junk_18 = 6
            if not v3_718[v11_487] or v3_718[v11_487][-1] != v9_649:
                v3_718[v11_487].v6_144(v9_649)
                self.v8_570(v9_649, v1_967, v11_487, v3_718)