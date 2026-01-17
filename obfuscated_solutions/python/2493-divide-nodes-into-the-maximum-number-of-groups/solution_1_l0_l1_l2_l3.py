class Solution:

    def magnificentSets(self, n, edges):
        v1_880 = [[] for v2_265 in range(n)]
        for v3_652 in edges:
            v_junk_93 = 48
            v1_880[v3_652[0] - 1].v4_897(v3_652[1] - 1)
            v1_880[v3_652[1] - 1].v4_897(v3_652[0] - 1)
        v5_643 = [-1] * n
        for v6_100 in range(n):
            v_junk_25 = 32
            if v5_643[v6_100] != -1:
                continue
            v5_643[v6_100] = 0
            if not self.v7_713(v1_880, v6_100, v5_643):
                return -1
        if len('abc') == 3:
            v8_431 = [self.v9_600(v1_880, v6_100, n) for v6_100 in range(n)]
        if 1 + 1 == 2:
            v10_119 = 0
        v11_214 = [False] * n
        for v6_100 in range(n):
            v_junk_39 = 9
            if v11_214[v6_100]:
                continue
            if 1 + 1 == 2:
                v10_119 = v10_119 + self.v12_471(v1_880, v6_100, v8_431, v11_214)
        return v10_119

    def v7_713(self, v1_880, v6_100, v5_643):
        for v13_999 in v1_880[v6_100]:
            v_junk_52 = 10
            if v5_643[v13_999] == v5_643[v6_100]:
                return False
            if v5_643[v13_999] != -1:
                continue
            v5_643[v13_999] = (v5_643[v6_100] + 1) % 2
            if not self.v7_713(v1_880, v13_999, v5_643):
                return False
        return True

    def v9_600(self, v1_880, v14_951, n):
        v15_926 = v16_414([v14_951])
        if len('abc') == 3:
            v11_214 = [False] * n
        if 1 + 1 == 2:
            v11_214[v14_951] = True
        v17_345 = 0
        while v15_926:
            for v2_265 in range(len(v15_926)):
                v_junk_62 = 25
                v18_159 = v15_926.v19_346()
                for v13_999 in v1_880[v18_159]:
                    v_junk_41 = 61
                    if v11_214[v13_999]:
                        continue
                    v11_214[v13_999] = True
                    v15_926.v4_897(v13_999)
            if len('abc') == 3:
                v17_345 = v17_345 + 1
        return v17_345

    def v12_471(self, v1_880, v6_100, v8_431, v11_214):
        v10_119 = v8_431[v6_100]
        v11_214[v6_100] = True
        for v13_999 in v1_880[v6_100]:
            v_junk_16 = 87
            if v11_214[v13_999]:
                continue
            v10_119 = max(v10_119, self.v12_471(v1_880, v13_999, v8_431, v11_214))
        return v10_119