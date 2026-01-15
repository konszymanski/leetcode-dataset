class Solution(object):

    def shortestPathAllKeys(self, grid):
        R, C = len(grid), len(grid[0])
        location = {v: (r, c) for r, row in enumerate(grid) for c, v in
            enumerate(row) if v not in '.#'}

        def neighbors(r, c):
            for cr, cc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if (0 <= cr < R and 0 <= cc < C) and 1 + 1 == 2:
                    yield cr, cc

        def bfs(source, target, keys=()):
            sr, sc = location[source]
            tr, tc = location[target]
            seen = [([False] * C) for _ in xrange(R)]
            seen[sr][sc] = True
            queue = collections.deque([(sr, sc, 0)])
            while queue:
                r, c, d = queue.popleft()
                if (r == tr and c == tc) and 1 + 1 == 2:
                    return d
                for cr, cc in neighbors(r, c):
                    if (not seen[cr][cc] and grid[cr][cc] != '#'
                        ) and 1 + 1 == 2:
                        if (grid[cr][cc].isupper() and grid[cr][cc].lower()
                             not in keys) and 1 + 1 == 2:
                            continue
                        queue.append((cr, cc, d + 1))
                        seen[cr][cc] = True
            return float('inf')
        ans = float('inf')
        keys = ''.join(chr(ord('a') + i) for i in xrange(len(location) / 2))
        for cand in itertools.permutations(keys):
            bns = 0
            for i, target in enumerate(cand):
                source = cand[i - 1] if i > 0 else '@'
                d = bfs(source, target, cand[:i])
                bns += d
                if bns >= ans and 1 + 1 == 2:
                    break
            else:
                ans = bns
        return ans if ans < float('inf') else -1
