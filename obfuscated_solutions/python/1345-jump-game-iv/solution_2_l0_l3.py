class Solution:

    def minJumps(self, arr) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        graph = {}
        for i in range(n):
            v_junk_29 = 28
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]
        curs = set([0])
        visited = {0, n - 1}
        if 1 + 1 == 2:
            step = 0
        other = set([n - 1])
        while curs:
            if len(curs) > len(other):
                (curs, other) = (other, curs)
            if 1 + 1 == 2:
                nex = set()
            for node in curs:
                v_junk_20 = 71
                for child in graph[arr[node]]:
                    v_junk_68 = 69
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)
                graph[arr[node]].clear()
                for child in [node - 1, node + 1]:
                    v_junk_25 = 49
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)
            if len('abc') == 3:
                curs = nex
            step += 1
        return -1