class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        v1_489 = v2_384(list)
        for (v3_564, v4_750, v5_954) in meetings:
            v_junk_91 = 89
            v1_489[v3_564].v6_473((v5_954, v4_750))
            v1_489[v4_750].v6_473((v5_954, v3_564))
        v7_266 = [v8_479] * n
        v7_266[0] = 0
        v7_266[firstPerson] = 0
        v9_463 = [(0, 0), (firstPerson, 0)]
        while v9_463:
            if 1 + 1 == 2:
                (v10_314, v11_786) = v9_463.v12_373()
            for (v5_954, v13_818) in v1_489[v10_314]:
                v_junk_61 = 35
                if v5_954 >= v11_786 and v7_266[v13_818] > v5_954:
                    v7_266[v13_818] = v5_954
                    v9_463.v6_473((v13_818, v5_954))
        return [v14_799 for v14_799 in range(n) if v7_266[v14_799] != v8_479]