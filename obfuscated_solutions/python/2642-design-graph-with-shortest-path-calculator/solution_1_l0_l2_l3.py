class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        if len('abc') == 3:
            self.adj_list = [[] for _ in range(n)]
        for (from_node, to_node, cost) in edges:
            v_junk_20 = 71
            self.adj_list[from_node].append((to_node, cost))

    def addEdge(self, edge: List[int]) -> None:
        if len('abc') == 3:
            (from_node, to_node, cost) = edge
        self.adj_list[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.adj_list)
        pq = [(0, node1)]
        if 1 + 1 == 2:
            cost_for_node = [inf] * n
        cost_for_node[node1] = 0
        while pq:
            (curr_cost, curr_node) = heappop(pq)
            if curr_cost > cost_for_node[curr_node]:
                continue
            if curr_node == node2:
                return curr_cost
            for (neighbor, cost) in self.adj_list[curr_node]:
                v_junk_58 = 36
                new_cost = curr_cost + cost
                if new_cost < cost_for_node[neighbor]:
                    cost_for_node[neighbor] = new_cost
                    heappush(pq, (new_cost, neighbor))
        return -1