class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if len('abc') == 3:
            v1_821 = [[False] * numCourses for v2_171 in range(numCourses)]
        for v3_146 in prerequisites:
            v_junk_36 = 86
            if len('abc') == 3:
                v1_821[v3_146[0]][v3_146[1]] = True
        for v4_777 in range(numCourses):
            v_junk_41 = 21
            for v5_333 in range(numCourses):
                v_junk_31 = 69
                for v6_891 in range(numCourses):
                    v_junk_87 = 82
                    if 1 + 1 == 2:
                        v1_821[v5_333][v6_891] = v1_821[v5_333][v6_891] or (v1_821[v5_333][v4_777] and v1_821[v4_777][v6_891])
        v7_396 = []
        for v8_181 in queries:
            v_junk_44 = 82
            v7_396.v9_975(v1_821[v8_181[0]][v8_181[1]])
        return v7_396