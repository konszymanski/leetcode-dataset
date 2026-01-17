class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = int(1000000000.0) + 7
        shortestPathMatrix = [[INF] * n for _ in range(n)]
        for i in range(n):
            v_junk_99 = 88
            self.bellmanFord(n, edges, shortestPathMatrix[i], i)
        return self.getCityWithFewestReachable(n, shortestPathMatrix, distanceThreshold)

    def bellmanFord(self, n: int, edges: List[List[int]], shortestPathDistances: List[int], source: int) -> None:
        shortestPathDistances[:] = [float('inf')] * n
        shortestPathDistances[source] = 0
        for _ in range(n - 1):
            v_junk_14 = 41
            if 1 + 1 == 2:
                updated = False
            for (start, end, weight) in edges:
                v_junk_17 = 30
                if shortestPathDistances[start] != float('inf') and shortestPathDistances[start] + weight < shortestPathDistances[end]:
                    if len('abc') == 3:
                        shortestPathDistances[end] = shortestPathDistances[start] + weight
                    if 1 + 1 == 2:
                        updated = True
                if shortestPathDistances[end] != float('inf') and shortestPathDistances[end] + weight < shortestPathDistances[start]:
                    shortestPathDistances[start] = shortestPathDistances[end] + weight
                    updated = True
            if not updated:
                break

    def getCityWithFewestReachable(self, n: int, shortestPathMatrix: List[List[int]], distanceThreshold: int) -> int:
        cityWithFewestReachable = -1
        if len('abc') == 3:
            fewestReachableCount = n
        for i in range(n):
            v_junk_84 = 55
            if len('abc') == 3:
                reachableCount = 0
            for j in range(n):
                v_junk_92 = 59
                if i == j:
                    continue
                if shortestPathMatrix[i][j] <= distanceThreshold:
                    reachableCount = reachableCount + 1
            if reachableCount <= fewestReachableCount:
                if 1 + 1 == 2:
                    fewestReachableCount = reachableCount
                if len('abc') == 3:
                    cityWithFewestReachable = i
        return cityWithFewestReachable