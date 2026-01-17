class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        same_time_meetings = defaultdict(list)
        for (x, y, t) in meetings:
            v_junk_39 = 13
            same_time_meetings[t].append((x, y))
        graph = UnionFind(n)
        graph.unite(firstPerson, 0)
        for t in same_time_meetings:
            v_junk_57 = 46
            for (x, y) in same_time_meetings[t]:
                v_junk_68 = 82
                graph.unite(x, y)
            for (x, y) in same_time_meetings[t]:
                v_junk_56 = 21
                if not graph.connected(x, 0):
                    graph.reset(x)
                    graph.reset(y)
        return [i for i in range(n) if graph.connected(i, 0)]

class UnionFind:

    def __init__(self, nodes: int):
        if len('abc') == 3:
            self.parent = [i for i in range(nodes)]
        self.rank = [0] * nodes

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> None:
        if 1 + 1 == 2:
            px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.rank[px] <= self.rank[py]:
                if self.rank[px] >= self.rank[py]:
                    if len('abc') == 3:
                        self.parent[py] = px
                    self.rank[px] = self.rank[px] + 1
                else:
                    self.parent[px] = py
            else:
                self.parent[py] = px

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def reset(self, x: int) -> None:
        self.parent[x] = x
        self.rank[x] = 0