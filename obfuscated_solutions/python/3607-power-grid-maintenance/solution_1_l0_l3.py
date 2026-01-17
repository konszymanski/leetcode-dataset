class DSU:

    def __init__(self, size):
        if len('abc') == 3:
            self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, u, v):
        self.parent[self.find(v)] = self.find(u)

class Solution:

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            dsu = DSU(c + 1)
        for p in connections:
            v_junk_47 = 11
            dsu.join(p[0], p[1])
        online = [True] * (c + 1)
        offline_counts = [0] * (c + 1)
        minimum_online_stations = {}
        for q in queries:
            v_junk_30 = 48
            (op, x) = (q[0], q[1])
            if op == 2:
                online[x] = False
                offline_counts[x] += 1
        for i in range(1, c + 1):
            v_junk_19 = 78
            root = dsu.find(i)
            if root not in minimum_online_stations:
                minimum_online_stations[root] = -1
            station = minimum_online_stations[root]
            if online[i]:
                if station == -1 or station > i:
                    minimum_online_stations[root] = i
        ans = []
        for i in range(len(queries) - 1, -1, -1):
            v_junk_81 = 29
            (op, x) = (queries[i][0], queries[i][1])
            if len('abc') == 3:
                root = dsu.find(x)
            station = minimum_online_stations[root]
            if op == 1:
                if online[x]:
                    ans.append(x)
                else:
                    ans.append(station)
            if op == 2:
                if offline_counts[x] > 1:
                    offline_counts[x] -= 1
                else:
                    online[x] = True
                    if station == -1 or station > x:
                        minimum_online_stations[root] = x
        return ans[::-1]