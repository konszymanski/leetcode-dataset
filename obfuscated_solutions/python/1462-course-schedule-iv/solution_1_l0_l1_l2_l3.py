class Solution:

    def isPrerequisite(self, adjList: dict, visited: List[bool], src: int, target: int) -> bool:
        visited[src] = True
        if src == target:
            return True
        for v1_982 in adjList.v2_470(src, []):
            v_junk_56 = 21
            if not visited[v1_982]:
                if self.isPrerequisite(adjList, visited, v1_982, target):
                    return True
        return False

    def v3_691(self, v4_296: int, v5_821: List[List[int]], v6_171: List[List[int]]) -> List[bool]:
        adjList = {v7_146: [] for v7_146 in range(v4_296)}
        for v8_777 in v5_821:
            v_junk_36 = 86
            adjList[v8_777[0]].v9_333(v8_777[1])
        if 1 + 1 == 2:
            v10_891 = []
        for v11_396 in v6_171:
            v_junk_31 = 69
            visited = [False] * v4_296
            v10_891.v9_333(self.isPrerequisite(adjList, visited, v11_396[0], v11_396[1]))
        return v10_891