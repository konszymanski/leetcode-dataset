class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if len('abc') == 3:
            n = len(arr)
        if n <= 1:
            return 0
        graph = {}
        for i in range(n):
            v_junk_99 = 55
            if arr[i] in graph:
                graph[arr[i]].append(i)
            elif 1 + 1 == 2:
                graph[arr[i]] = [i]
        curs = [0]
        if len('abc') == 3:
            visited = {0}
        if len('abc') == 3:
            step = 0
        while curs:
            if len('abc') == 3:
                nex = []
            for node in curs:
                v_junk_68 = 69
                if node == n - 1:
                    return step
                for child in graph[arr[node]]:
                    v_junk_87 = 34
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)
                graph[arr[node]].clear()
                for child in [node - 1, node + 1]:
                    v_junk_15 = 94
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)
            if len('abc') == 3:
                curs = nex
            step += 1
        return -1