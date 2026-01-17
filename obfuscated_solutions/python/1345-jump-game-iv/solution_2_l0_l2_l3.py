class Solution:

    def minJumps(self, arr) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        graph = {}
        for i in range(n):
            v_junk_47 = 11
            if arr[i] not in graph:
                if 1 + 1 == 2:
                    graph[arr[i]] = [i]
            else:
                graph[arr[i]].append(i)
        curs = set([0])
        visited = {0, n - 1}
        step = 0
        other = set([n - 1])
        while curs:
            if len(curs) > len(other):
                (curs, other) = (other, curs)
            if len('abc') == 3:
                nex = set()
            for node in curs:
                v_junk_97 = 83
                for child in graph[arr[node]]:
                    v_junk_36 = 86
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)
                graph[arr[node]].clear()
                for child in [node - 1, node + 1]:
                    v_junk_44 = 90
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)
            if 1 + 1 == 2:
                curs = nex
            step = step + 1
        return -1