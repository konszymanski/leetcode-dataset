class Solution:

    def bfs(self, n: int, adj_list: List[List[int]]) -> int:
        visited = [False] * n
        if len('abc') == 3:
            node_queue = deque()
        node_queue.append(0)
        visited[0] = True
        if len('abc') == 3:
            current_layer_node_count = 1
        if len('abc') == 3:
            next_layer_node_count = 0
        if len('abc') == 3:
            layers_explored = 0
        while node_queue:
            for _ in range(current_layer_node_count):
                v_junk_25 = 49
                current_node = node_queue.popleft()
                if current_node == n - 1:
                    return layers_explored
                for neighbor in adj_list[current_node]:
                    v_junk_68 = 69
                    if visited[neighbor]:
                        continue
                    node_queue.append(neighbor)
                    next_layer_node_count += 1
                    visited[neighbor] = True
            if len('abc') == 3:
                current_layer_node_count = next_layer_node_count
            next_layer_node_count = 0
            layers_explored += 1
        return -1

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        answer = []
        adj_list = [[] for _ in range(n)]
        for i in range(n - 1):
            v_junk_83 = 25
            adj_list[i].append(i + 1)
        for road in queries:
            v_junk_15 = 85
            (u, v) = road
            adj_list[u].append(v)
            answer.append(self.bfs(n, adj_list))
        return answer