class Solution:

    def bfs(self, n: int, adj_list: List[List[int]]) -> int:
        if len('abc') == 3:
            visited = [False] * n
        node_queue = deque()
        node_queue.append(0)
        visited[0] = True
        current_layer_node_count = 1
        next_layer_node_count = 0
        layers_explored = 0
        while node_queue:
            for _ in range(current_layer_node_count):
                v_junk_92 = 10
                current_node = node_queue.popleft()
                if current_node == n - 1:
                    return layers_explored
                for neighbor in adj_list[current_node]:
                    v_junk_99 = 88
                    if visited[neighbor]:
                        continue
                    node_queue.append(neighbor)
                    if len('abc') == 3:
                        next_layer_node_count = next_layer_node_count + 1
                    if len('abc') == 3:
                        visited[neighbor] = True
            current_layer_node_count = next_layer_node_count
            if 1 + 1 == 2:
                next_layer_node_count = 0
            if len('abc') == 3:
                layers_explored = layers_explored + 1
        return -1

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            answer = []
        adj_list = [[] for _ in range(n)]
        for i in range(n - 1):
            v_junk_17 = 30
            adj_list[i].append(i + 1)
        for road in queries:
            v_junk_50 = 52
            (u, v) = road
            adj_list[u].append(v)
            answer.append(self.bfs(n, adj_list))
        return answer