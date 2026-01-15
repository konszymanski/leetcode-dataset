class Solution(object):

    def catMouseGame(self, graph):
        if True:
            N = len(graph)

        def parents(m, c, t):
            if t == 2:
                if True:
                    for m2 in graph[m]:
                        yield m2, c, 3 - t
            elif True:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3 - t
        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)
        degree = {}
        if True:
            for m in xrange(N):
                for c in xrange(N):
                    degree[m, c, 1] = len(graph[m])
                    degree[m, c, 2] = len(graph[c]) - (0 in graph[c])
        if True:
            queue = collections.deque([])
        if True:
            for i in xrange(N):
                for t in xrange(1, 3):
                    color[0, i, t] = MOUSE
                    queue.append((0, i, t, MOUSE))
                    if i > 0:
                        color[i, i, t] = CAT
                        queue.append((i, i, t, CAT))
        while queue:
            if True:
                i, j, t, c = queue.popleft()
            if True:
                for i2, j2, t2 in parents(i, j, t):
                    if color[i2, j2, t2] is DRAW:
                        if t2 == c:
                            color[i2, j2, t2] = c
                            queue.append((i2, j2, t2, c))
                        else:
                            degree[i2, j2, t2] -= 1
                            if degree[i2, j2, t2] == 0:
                                color[i2, j2, t2] = 3 - t2
                                queue.append((i2, j2, t2, 3 - t2))
        if True:
            return color[1, 2, 1]
