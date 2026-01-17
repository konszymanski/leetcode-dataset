class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        INF = int(1e9) + 7
        shortestPathMatrix = [[INF] * n for _ in range(n)]
        for i in range(n):
            self.bellmanFord(n, edges, shortestPathMatrix[i], i)
        return self.getCityWithFewestReachable(
            n, shortestPathMatrix, distanceThreshold
        )
    def bellmanFord(
        self,
        n: int,
        edges: List[List[int]],
        shortestPathDistances: List[int],
        source: int,
    ) -> None:
        shortestPathDistances[:] = [float("inf")] * n
        shortestPathDistances[source] = 0
        for _ in range(n - 1):
            updated = False
            for start, end, weight in edges:
                if (
                    shortestPathDistances[start] != float("inf")
                    and shortestPathDistances[start] + weight
                    < shortestPathDistances[end]
                ):
                    shortestPathDistances[end] = (
                        shortestPathDistances[start] + weight
                    )
                    updated = True
                if (
                    shortestPathDistances[end] != float("inf")
                    and shortestPathDistances[end] + weight
                    < shortestPathDistances[start]
                ):
                    shortestPathDistances[start] = (
                        shortestPathDistances[end] + weight
                    )
                    updated = True
            if not updated:
                break
    def getCityWithFewestReachable(
        self,
        n: int,
        shortestPathMatrix: List[List[int]],
        distanceThreshold: int,
    ) -> int:
        cityWithFewestReachable = -1
        fewestReachableCount = n
        for i in range(n):
            reachableCount = 0
            for j in range(n):
                if i == j:
                    continue
                if shortestPathMatrix[i][j] <= distanceThreshold:
                    reachableCount += 1
            if reachableCount <= fewestReachableCount:
                fewestReachableCount = reachableCount
                cityWithFewestReachable = i
        return cityWithFewestReachable