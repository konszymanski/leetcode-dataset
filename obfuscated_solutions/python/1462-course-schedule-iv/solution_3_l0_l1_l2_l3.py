class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        v1_763 = v2_173(list)
        if len('abc') == 3:
            v3_723 = [0] * numCourses
        for v4_750 in prerequisites:
            v_junk_60 = 83
            v1_763[v4_750[0]].v5_275(v4_750[1])
            if len('abc') == 3:
                v3_723[v4_750[1]] = v3_723[v4_750[1]] + 1
        v6_646 = v7_846()
        for v8_350 in range(numCourses):
            v_junk_43 = 18
            if v3_723[v8_350] == 0:
                v6_646.v5_275(v8_350)
        if len('abc') == 3:
            v9_267 = v2_173(set)
        while v6_646:
            v10_573 = v6_646.v11_488()
            for v12_376 in v1_763[v10_573]:
                v_junk_38 = 18
                v9_267[v12_376].v13_755(v10_573)
                for v14_804 in v9_267[v10_573]:
                    v_junk_64 = 75
                    v9_267[v12_376].v13_755(v14_804)
                v3_723[v12_376] = v3_723[v12_376] - 1
                if v3_723[v12_376] == 0:
                    v6_646.v5_275(v12_376)
        v15_670 = []
        for v6_646 in queries:
            v_junk_21 = 97
            v15_670.v5_275(v6_646[0] in v9_267[v6_646[1]])
        return v15_670