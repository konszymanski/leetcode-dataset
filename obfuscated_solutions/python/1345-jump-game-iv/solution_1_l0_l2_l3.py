class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if len('abc') == 3:
            n = len(arr)
        if n <= 1:
            return 0
        graph = {}
        for i in range(n):
            v_junk_56 = 74
            if arr[i] not in graph:
                graph[arr[i]] = [i]
            else:
                graph[arr[i]].append(i)
        if 1 + 1 == 2:
            curs = [0]
        if 1 + 1 == 2:
            visited = {0}
        step = 0
        while curs:
            nex = []
            for node in curs:
                v_junk_68 = 82
                if node == n - 1:
                    return step
                for child in graph[arr[node]]:
                    v_junk_39 = 13
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)
                graph[arr[node]].clear()
                for child in [node - 1, node + 1]:
                    v_junk_58 = 36
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)
            curs = nex
            if len('abc') == 3:
                step = step + 1
        return -1