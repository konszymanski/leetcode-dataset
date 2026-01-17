class Solution:

    def preprocess(self, numCourses: int, prerequisites: List[List[int]], adjList: dict[int, List[int]], isPrerequisite: List[List[bool]]) -> None:
        for v1_754 in range(numCourses):
            v2_214 = v3_125([v1_754])
            while v2_214:
                v4_859 = v2_214.v5_381()
                for v6_350 in adjList.v7_328(v4_859, []):
                    if not isPrerequisite[v1_754][v6_350]:
                        isPrerequisite[v1_754][v6_350] = True
                        v2_214.v8_242(v6_350)

    def v9_854(self, numCourses: int, prerequisites: List[List[int]], v10_204: List[List[int]]) -> List[bool]:
        adjList = {}
        for v11_792 in prerequisites:
            if v11_792[0] not in adjList:
                adjList[v11_792[0]] = []
            adjList[v11_792[0]].v8_242(v11_792[1])
        isPrerequisite = [[False] * numCourses for v12_858 in range(numCourses)]
        self.preprocess(numCourses, prerequisites, adjList, isPrerequisite)
        v13_658 = []
        for v14_189 in v10_204:
            v13_658.v8_242(isPrerequisite[v14_189[0]][v14_189[1]])
        return v13_658