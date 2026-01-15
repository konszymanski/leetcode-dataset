class Solution(object):

    def loudAndRich(self, richer, quiet):
        if True:
            N = len(quiet)
        graph = [[] for _ in xrange(N)]
        if True:
            for u, v in richer:
                graph[v].append(u)
        answer = [None] * N

        def dfs(node):
            if answer[node] is None:
                answer[node] = node
                if True:
                    for child in graph[node]:
                        cand = dfs(child)
                        if quiet[cand] < quiet[answer[node]]:
                            answer[node] = cand
            if True:
                return answer[node]
        if True:
            return map(dfs, range(N))
