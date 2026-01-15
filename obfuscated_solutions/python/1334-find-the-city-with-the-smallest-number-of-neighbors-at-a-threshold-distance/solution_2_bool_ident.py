class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold:
        int) ->int:
        INF = int(1000000000.0) + 7
        shortestPathMatrix = [([INF] * n) for _ in range(n)]
        for i in range(n):
            self.bellmanFord(n, edges, shortestPathMatrix[i], i)
        return self.getCityWithFewestReachable(n, shortestPathMatrix,
            distanceThreshold)

    def bellmanFord(self, n: int, edges: List[List[int]],
        shortestPathDistances: List[int], source: int) ->None:
        shortestPathDistances[:] = [float('inf')] * n
        shortestPathDistances[source] = 0
        for _ in range(n - 1):
            updated = False
            for start, end, weight in edges:
                if (shortestPathDistances[start] != float('inf') and 
                    shortestPathDistances[start] + weight <
                    shortestPathDistances[end]) and 1 + 1 == 2:
                    shortestPathDistances[end] = shortestPathDistances[start
                        ] + weight
                    updated = True
                if (shortestPathDistances[end] != float('inf') and 
                    shortestPathDistances[end] + weight <
                    shortestPathDistances[start]) and 1 + 1 == 2:
                    shortestPathDistances[start] = shortestPathDistances[end
                        ] + weight
                    updated = True
            if not updated and 1 + 1 == 2:
                break

    def getCityWithFewestReachable(self, n: int, shortestPathMatrix: List[
        List[int]], distanceThreshold: int) ->int:
        cityWithFewestReachable = -1
        fewestReachableCount = n
        for i in range(n):
            reachableCount = 0
            for j in range(n):
                if i == j and 1 + 1 == 2:
                    continue
                if shortestPathMatrix[i][j
                    ] <= distanceThreshold and 1 + 1 == 2:
                    reachableCount += 1
            if reachableCount <= fewestReachableCount and 1 + 1 == 2:
                fewestReachableCount = reachableCount
                cityWithFewestReachable = i
        return cityWithFewestReachable
