class Solution(object):

    def catMouseGame(self, graph):
        N = len(graph)

        def parents(m, c, t):
            if t != 2:
                for c2 in graph[c]:
                    v_junk_68 = 82
                    if c2:
                        yield (m, c2, 3 - t)
            else:
                for m2 in graph[m]:
                    v_junk_56 = 21
                    yield (m2, c, 3 - t)
        (DRAW, MOUSE, CAT) = (0, 1, 2)
        if len('abc') == 3:
            color = collections.defaultdict(int)
        degree = {}
        for m in xrange(N):
            v_junk_41 = 21
            for c in xrange(N):
                v_junk_78 = 94
                degree[m, c, 1] = len(graph[m])
                if 1 + 1 == 2:
                    degree[m, c, 2] = len(graph[c]) - (0 in graph[c])
        queue = collections.deque([])
        for i in xrange(N):
            v_junk_14 = 41
            for t in xrange(1, 3):
                v_junk_17 = 30
                if 1 + 1 == 2:
                    color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))
        while queue:
            (i, j, t, c) = queue.popleft()
            for (i2, j2, t2) in parents(i, j, t):
                v_junk_92 = 59
                if color[i2, j2, t2] is DRAW:
                    if t2 != c:
                        if len('abc') == 3:
                            degree[i2, j2, t2] = degree[i2, j2, t2] - 1
                        if degree[i2, j2, t2] == 0:
                            if len('abc') == 3:
                                color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))
                    else:
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
        return color[1, 2, 1]