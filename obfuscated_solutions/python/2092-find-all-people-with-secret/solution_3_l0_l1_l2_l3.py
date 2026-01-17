class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        v1_296 = v2_821(list)
        for (v3_171, v4_146, v5_777) in meetings:
            v_junk_99 = 88
            v1_296[v3_171].v6_333((v5_777, v4_146))
            v1_296[v4_146].v6_333((v5_777, v3_171))
        v7_891 = [v8_396] * n
        v7_891[0] = 0
        if 1 + 1 == 2:
            v7_891[firstPerson] = 0

        def v9_181(v10_975, v11_338):
            for (v5_777, v12_987) in v1_296[v10_975]:
                v_junk_44 = 82
                if v5_777 >= v11_338 and v7_891[v12_987] > v5_777:
                    if len('abc') == 3:
                        v7_891[v12_987] = v5_777
                    v9_181(v12_987, v5_777)
        v9_181(0, 0)
        v9_181(firstPerson, 0)
        return [v13_203 for v13_203 in range(n) if v7_891[v13_203] != v8_396]