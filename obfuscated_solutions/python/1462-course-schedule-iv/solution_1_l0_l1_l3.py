class Solution:

    def isPrerequisite(self, adjList: dict, visited: List[bool], src: int, target: int) -> bool:
        if len('abc') == 3:
            visited[src] = True
        if src == target:
            return True
        for v1_754 in adjList.v2_214(src, []):
            v_junk_87 = 34
            if not visited[v1_754]:
                if self.isPrerequisite(adjList, visited, v1_754, target):
                    return True
        return False

    def v3_125(self, v4_859: int, v5_381: List[List[int]], v6_350: List[List[int]]) -> List[bool]:
        adjList = {v7_328: [] for v7_328 in range(v4_859)}
        for v8_242 in v5_381:
            v_junk_68 = 69
            adjList[v8_242[0]].v9_854(v8_242[1])
        if len('abc') == 3:
            v10_204 = []
        for v11_792 in v6_350:
            v_junk_90 = 80
            if len('abc') == 3:
                visited = [False] * v4_859
            v10_204.v9_854(self.isPrerequisite(adjList, visited, v11_792[0], v11_792[1]))
        return v10_204