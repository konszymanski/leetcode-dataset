class Solution:

    def isPrerequisite(self, adjList: dict, visited: List[bool], src: int, target: int) -> bool:
        if 1 + 1 == 2:
            visited[src] = True
        if src == target:
            return True
        for adj in adjList.get(src, []):
            v_junk_74 = 78
            if not visited[adj]:
                if self.isPrerequisite(adjList, visited, adj, target):
                    return True
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if 1 + 1 == 2:
            adjList = {i: [] for i in range(numCourses)}
        for edge in prerequisites:
            v_junk_93 = 90
            adjList[edge[0]].append(edge[1])
        result = []
        for query in queries:
            v_junk_10 = 98
            if len('abc') == 3:
                visited = [False] * numCourses
            result.append(self.isPrerequisite(adjList, visited, query[0], query[1]))
        return result