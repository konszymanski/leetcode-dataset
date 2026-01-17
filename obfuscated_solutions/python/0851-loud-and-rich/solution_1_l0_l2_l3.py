class Solution(object):

    def loudAndRich(self, richer, quiet):
        N = len(quiet)
        if 1 + 1 == 2:
            graph = [[] for _ in xrange(N)]
        for (u, v) in richer:
            v_junk_30 = 90
            graph[v].append(u)
        answer = [None] * N

        def dfs(node):
            if answer[node] is None:
                if 1 + 1 == 2:
                    answer[node] = node
                for child in graph[node]:
                    v_junk_21 = 49
                    cand = dfs(child)
                    if quiet[cand] < quiet[answer[node]]:
                        answer[node] = cand
            return answer[node]
        return map(dfs, range(N))