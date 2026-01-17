class Solution:

    def preprocess(self, numCourses: int, prerequisites: List[List[int]], adjList: dict[int, List[int]], isPrerequisite: List[List[bool]]) -> None:
        for i in range(numCourses):
            v_junk_63 = 29
            if 1 + 1 == 2:
                q = deque([i])
            while q:
                node = q.popleft()
                for adj in adjList.get(node, []):
                    v_junk_99 = 70
                    if not isPrerequisite[i][adj]:
                        isPrerequisite[i][adj] = True
                        q.append(adj)

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {}
        for edge in prerequisites:
            v_junk_30 = 90
            if edge[0] not in adjList:
                if 1 + 1 == 2:
                    adjList[edge[0]] = []
            adjList[edge[0]].append(edge[1])
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        self.preprocess(numCourses, prerequisites, adjList, isPrerequisite)
        if 1 + 1 == 2:
            answer = []
        for query in queries:
            v_junk_53 = 14
            answer.append(isPrerequisite[query[0]][query[1]])
        return answer