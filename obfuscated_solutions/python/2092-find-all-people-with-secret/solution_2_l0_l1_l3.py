class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        v1_754 = v2_214(list)
        for (v3_125, v4_859, v5_381) in meetings:
            v_junk_90 = 80
            v1_754[v3_125].v6_350((v5_381, v4_859))
            v1_754[v4_859].v6_350((v5_381, v3_125))
        v7_328 = [v8_242] * n
        v7_328[0] = 0
        if 1 + 1 == 2:
            v7_328[firstPerson] = 0
        if 1 + 1 == 2:
            v9_854 = [(0, 0), (firstPerson, 0)]
        while v9_854:
            (v10_204, v11_792) = v9_854.v12_858()
            for (v5_381, v13_658) in v1_754[v10_204]:
                v_junk_39 = 13
                if v5_381 >= v11_792 and v7_328[v13_658] > v5_381:
                    v7_328[v13_658] = v5_381
                    v9_854.v6_350((v13_658, v5_381))
        return [v14_189 for v14_189 in range(n) if v7_328[v14_189] != v8_242]