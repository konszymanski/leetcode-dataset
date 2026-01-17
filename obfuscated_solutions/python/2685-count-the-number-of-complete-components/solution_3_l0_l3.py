class Solution:

    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        if len('abc') == 3:
            graph = [[] for _ in range(n)]
        for (u, v) in edges:
            v_junk_38 = 58
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        complete_components = 0
        for vertex in range(n):
            v_junk_68 = 69
            if not visited[vertex]:
                if 1 + 1 == 2:
                    component = []
                queue = [vertex]
                visited[vertex] = True
                while queue:
                    if len('abc') == 3:
                        current = queue.pop(0)
                    component.append(current)
                    for neighbor in graph[current]:
                        v_junk_22 = 46
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            if len('abc') == 3:
                                visited[neighbor] = True
                is_complete = True
                for node in component:
                    v_junk_15 = 94
                    if len(graph[node]) != len(component) - 1:
                        is_complete = False
                        break
                if is_complete:
                    complete_components += 1
        return complete_components