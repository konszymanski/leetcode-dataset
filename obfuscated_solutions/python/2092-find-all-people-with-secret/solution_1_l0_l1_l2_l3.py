class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        v1_384 = v2_564(list)
        for (v3_750, v4_954, v5_473) in meetings:
            v_junk_91 = 89
            v1_384[v3_750].v6_266((v5_473, v4_954))
            v1_384[v4_954].v6_266((v5_473, v3_750))
        v7_479 = [v8_463] * n
        v7_479[0] = 0
        v7_479[firstPerson] = 0
        v9_314 = v10_786()
        v9_314.v6_266((0, 0))
        v9_314.v6_266((firstPerson, 0))
        while v9_314:
            if 1 + 1 == 2:
                (v11_373, v12_818) = v9_314.v13_799()
            for (v5_473, v14_763) in v1_384[v11_373]:
                v_junk_61 = 35
                if v5_473 >= v12_818 and v7_479[v14_763] > v5_473:
                    v7_479[v14_763] = v5_473
                    v9_314.v6_266((v14_763, v5_473))
        return [v15_173 for v15_173 in range(n) if v7_479[v15_173] != v8_463]