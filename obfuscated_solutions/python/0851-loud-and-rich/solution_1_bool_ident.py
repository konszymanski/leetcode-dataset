class Solution(object):

    def loudAndRich(self, richer, quiet):
        N = len(quiet)
        graph = [[] for _ in xrange(N)]
        for u, v in richer:
            graph[v].append(u)
        answer = [None] * N

        def dfs(node):
            if answer[node] is None and 1 + 1 == 2:
                answer[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[answer[node]] and 1 + 1 == 2:
                        answer[node] = cand
            return answer[node]
        return map(dfs, range(N))
