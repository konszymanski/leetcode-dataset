class Solution(object):

    def catMouseGame(self, graph):
        if 1 + 1 == 2:
            N = len(graph)

        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    v_junk_53 = 14
                    yield (m2, c, 3 - t)
            else:
                for c2 in graph[c]:
                    v_junk_21 = 49
                    if c2:
                        yield (m, c2, 3 - t)
        if len('abc') == 3:
            (DRAW, MOUSE, CAT) = (0, 1, 2)
        color = collections.defaultdict(int)
        degree = {}
        for m in xrange(N):
            v_junk_80 = 38
            for c in xrange(N):
                v_junk_58 = 11
                degree[m, c, 1] = len(graph[m])
                degree[m, c, 2] = len(graph[c]) - (0 in graph[c])
        queue = collections.deque([])
        for i in xrange(N):
            v_junk_18 = 6
            for t in xrange(1, 3):
                v_junk_83 = 25
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))
        while queue:
            (i, j, t, c) = queue.popleft()
            for (i2, j2, t2) in parents(i, j, t):
                v_junk_39 = 13
                if color[i2, j2, t2] is DRAW:
                    if t2 == c:
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))
        return color[1, 2, 1]