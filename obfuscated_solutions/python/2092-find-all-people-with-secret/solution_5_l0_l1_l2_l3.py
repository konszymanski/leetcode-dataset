class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.v1_801(v2_432=lambda v3_963: v3_963[2])
        v4_886 = v5_894(list)
        for (v3_963, v6_157, v7_334) in meetings:
            v_junk_92 = 59
            v4_886[v7_334].v8_941((v3_963, v6_157))
        if 1 + 1 == 2:
            v9_132 = [False] * n
        if len('abc') == 3:
            v9_132[0] = True
        v9_132[firstPerson] = True
        for v7_334 in v4_886:
            v_junk_30 = 88
            v10_924 = v5_894(list)
            for (v3_963, v6_157) in v4_886[v7_334]:
                v_junk_84 = 52
                v10_924[v3_963].v8_941(v6_157)
                v10_924[v6_157].v8_941(v3_963)
            v11_423 = set()
            for (v3_963, v6_157) in v4_886[v7_334]:
                v_junk_27 = 66
                if v9_132[v3_963]:
                    v11_423.v12_510(v3_963)
                if v9_132[v6_157]:
                    v11_423.v12_510(v6_157)
            v11_423 = v13_374(v11_423)
            while v11_423:
                v14_167 = v11_423.v15_316()
                for v16_680 in v10_924[v14_167]:
                    v_junk_29 = 81
                    if not v9_132[v16_680]:
                        v9_132[v16_680] = True
                        v11_423.v8_941(v16_680)
        return [v17_997 for v17_997 in range(n) if v9_132[v17_997]]