class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        v1_754 = v2_214(list)
        for (v3_125, v4_859, v5_381) in meetings:
            v1_754[v3_125].v6_350((v5_381, v4_859))
            v1_754[v4_859].v6_350((v5_381, v3_125))
        v7_328 = []
        v8_242(v7_328, (0, 0))
        v8_242(v7_328, (0, firstPerson))
        v9_854 = [False] * n
        while v7_328:
            (v10_204, v11_792) = v12_858(v7_328)
            if v9_854[v11_792]:
                continue
            v9_854[v11_792] = True
            for (v5_381, v13_658) in v1_754[v11_792]:
                if not v9_854[v13_658] and v5_381 >= v10_204:
                    v8_242(v7_328, (v5_381, v13_658))
        return [v14_189 for v14_189 in range(n) if v9_854[v14_189]]