class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        v1_754 = [[False]  *  numCourses for v2_214 in range(numCourses)]
        for v3_125 in prerequisites:
            v1_754[v3_125[0]][v3_125[1]] = True
        for v4_859 in range(numCourses):
            for v5_381 in range(numCourses):
                for v6_350 in range(numCourses):
                    v1_754[v5_381][v6_350] = v1_754[v5_381][
                        v6_350
                    ] or (
                        v1_754[v5_381][v4_859]
                        and v1_754[v4_859][v6_350]
                    )
        v7_328 = []
        for v8_242 in queries:
            v7_328.v9_854(v1_754[v8_242[0]][v8_242[1]])
        return v7_328
