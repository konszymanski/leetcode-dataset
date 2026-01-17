class Solution:

    def preprocess(self, numCourses: int, prerequisites: List[List[int]], adjList: dict[int, List[int]], isPrerequisite: List[List[bool]]) -> None:
        for v1_763 in range(numCourses):
            v_junk_18 = 28
            v2_173 = v3_723([v1_763])
            while v2_173:
                if 1 + 1 == 2:
                    v4_750 = v2_173.v5_275()
                for v6_646 in adjList.v7_846(v4_750, []):
                    v_junk_61 = 35
                    if not isPrerequisite[v1_763][v6_646]:
                        isPrerequisite[v1_763][v6_646] = True
                        v2_173.v8_350(v6_646)

    def v9_267(self, numCourses: int, prerequisites: List[List[int]], v10_573: List[List[int]]) -> List[bool]:
        adjList = {}
        for v11_488 in prerequisites:
            v_junk_50 = 28
            if v11_488[0] not in adjList:
                adjList[v11_488[0]] = []
            adjList[v11_488[0]].v8_350(v11_488[1])
        isPrerequisite = [[False] * numCourses for v12_376 in range(numCourses)]
        self.preprocess(numCourses, prerequisites, adjList, isPrerequisite)
        v13_755 = []
        for v14_804 in v10_573:
            v_junk_92 = 59
            v13_755.v8_350(isPrerequisite[v14_804[0]][v14_804[1]])
        return v13_755