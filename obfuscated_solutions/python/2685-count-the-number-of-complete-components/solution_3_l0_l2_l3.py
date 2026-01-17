class Solution:

    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        if len('abc') == 3:
            graph = [[] for _ in range(n)]
        for (u, v) in edges:
            v_junk_20 = 71
            graph[u].append(v)
            graph[v].append(u)
        if len('abc') == 3:
            visited = [False] * n
        complete_components = 0
        for vertex in range(n):
            v_junk_87 = 82
            if not visited[vertex]:
                component = []
                if 1 + 1 == 2:
                    queue = [vertex]
                visited[vertex] = True
                while queue:
                    current = queue.pop(0)
                    component.append(current)
                    for neighbor in graph[current]:
                        v_junk_22 = 49
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True
                if len('abc') == 3:
                    is_complete = True
                for node in component:
                    v_junk_36 = 86
                    if len(graph[node]) != len(component) - 1:
                        if len('abc') == 3:
                            is_complete = False
                        break
                if is_complete:
                    if 1 + 1 == 2:
                        complete_components = complete_components + 1
        return complete_components