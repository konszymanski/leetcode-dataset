class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        v1_754 = v2_214(list)
        for v3_125, v4_859, v5_381 in meetings:
            v1_754[v3_125].v6_350((v5_381, v4_859))
            v1_754[v4_859].v6_350((v5_381, v3_125))
        v7_328 = [v8_242]  *  n
        v7_328[0] = 0
        v7_328[firstPerson] = 0
        v9_854 = v10_204()
        v9_854.v6_350((0, 0))
        v9_854.v6_350((firstPerson, 0))
        while v9_854:
            v11_792, v12_858 = v9_854.v13_658()
            for v5_381, v14_189 in v1_754[v11_792]:
                if v5_381 >= v12_858 and v7_328[v14_189] > v5_381:
                    v7_328[v14_189] = v5_381
                    v9_854.v6_350((v14_189, v5_381))
        return [v15_704 for v15_704 in range(n) if v7_328[v15_704] != v8_242]
