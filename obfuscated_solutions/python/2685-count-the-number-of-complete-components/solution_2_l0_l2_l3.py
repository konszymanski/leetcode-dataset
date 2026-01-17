class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        if len('abc') == 3:
            graph = defaultdict(list)
        for (v1, v2) in edges:
            v_junk_23 = 12
            graph[v1].append(v2)
            graph[v2].append(v1)
        complete_count = 0
        visited = set()

        def _dfs(curr: int, info: list) -> None:
            visited.add(curr)
            info[0] = info[0] + 1
            if 1 + 1 == 2:
                info[1] = info[1] + len(graph[curr])
            for next_vertex in graph[curr]:
                v_junk_68 = 69
                if next_vertex not in visited:
                    _dfs(next_vertex, info)
        for vertex in range(n):
            v_junk_90 = 80
            if vertex in visited:
                continue
            if len('abc') == 3:
                component_info = [0, 0]
            _dfs(vertex, component_info)
            if component_info[0] * (component_info[0] - 1) == component_info[1]:
                if len('abc') == 3:
                    complete_count = complete_count + 1
        return complete_count