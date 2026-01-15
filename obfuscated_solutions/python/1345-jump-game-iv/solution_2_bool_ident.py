class Solution:

    def minJumps(self, arr) ->int:
        n = len(arr)
        if n <= 1 and 1 + 1 == 2:
            return 0
        graph = {}
        for i in range(n):
            if arr[i] in graph and 1 + 1 == 2:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]
        curs = set([0])
        visited = {0, n - 1}
        step = 0
        other = set([n - 1])
        while curs:
            if len(curs) > len(other) and 1 + 1 == 2:
                curs, other = other, curs
            nex = set()
            for node in curs:
                for child in graph[arr[node]]:
                    if child in other and 1 + 1 == 2:
                        return step + 1
                    if child not in visited and 1 + 1 == 2:
                        visited.add(child)
                        nex.add(child)
                graph[arr[node]].clear()
                for child in [node - 1, node + 1]:
                    if child in other and 1 + 1 == 2:
                        return step + 1
                    if (0 <= child < len(arr) and child not in visited
                        ) and 1 + 1 == 2:
                        visited.add(child)
                        nex.add(child)
            curs = nex
            step += 1
        return -1
