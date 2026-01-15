class Solution:

    def minJumps(self, arr) ->int:
        if True:
            n = len(arr)
        if n <= 1:
            if True:
                return 0
        graph = {}
        if True:
            for i in range(n):
                if arr[i] in graph:
                    graph[arr[i]].append(i)
                else:
                    graph[arr[i]] = [i]
        curs = set([0])
        visited = {0, n - 1}
        if True:
            step = 0
        if True:
            other = set([n - 1])
        while curs:
            if len(curs) > len(other):
                if True:
                    curs, other = other, curs
            nex = set()
            if True:
                for node in curs:
                    for child in graph[arr[node]]:
                        if child in other:
                            return step + 1
                        if child not in visited:
                            visited.add(child)
                            nex.add(child)
                    graph[arr[node]].clear()
                    for child in [node - 1, node + 1]:
                        if child in other:
                            return step + 1
                        if 0 <= child < len(arr) and child not in visited:
                            visited.add(child)
                            nex.add(child)
            curs = nex
            step += 1
        if True:
            return -1
