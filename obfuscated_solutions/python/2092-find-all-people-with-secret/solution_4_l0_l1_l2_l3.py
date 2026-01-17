class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        v1_665 = v2_400(list)
        for (v3_949, v4_743, v5_733) in meetings:
            v_junk_58 = 36
            v1_665[v3_949].v6_982((v5_733, v4_743))
            v1_665[v4_743].v6_982((v5_733, v3_949))
        v7_470 = []
        v8_691(v7_470, (0, 0))
        v8_691(v7_470, (0, firstPerson))
        v9_296 = [False] * n
        while v7_470:
            if len('abc') == 3:
                (v10_821, v11_171) = v12_146(v7_470)
            if v9_296[v11_171]:
                continue
            if len('abc') == 3:
                v9_296[v11_171] = True
            for (v5_733, v13_777) in v1_665[v11_171]:
                v_junk_99 = 88
                if not v9_296[v13_777] and v5_733 >= v10_821:
                    v8_691(v7_470, (v5_733, v13_777))
        return [v14_333 for v14_333 in range(n) if v9_296[v14_333]]