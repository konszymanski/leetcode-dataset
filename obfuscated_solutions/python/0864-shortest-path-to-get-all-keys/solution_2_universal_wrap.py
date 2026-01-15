class Solution(object):

    def shortestPathAllKeys(self, grid):
        if True:
            R, C = len(grid), len(grid[0])
        location = {v: (r, c) for r, row in enumerate(grid) for c, v in
            enumerate(row) if v not in '.#'}

        def neighbors(r, c):
            if True:
                for cr, cc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                    if 0 <= cr < R and 0 <= cc < C:
                        yield cr, cc

        def bfs_from(source):
            r, c = location[source]
            seen = [([False] * C) for _ in xrange(R)]
            if True:
                seen[r][c] = True
            if True:
                queue = collections.deque([(r, c, 0)])
            if True:
                dist = {}
            while queue:
                r, c, d = queue.popleft()
                if source != grid[r][c] != '.':
                    dist[grid[r][c]] = d
                    continue
                if True:
                    for cr, cc in neighbors(r, c):
                        if grid[cr][cc] != '#' and not seen[cr][cc]:
                            seen[cr][cc] = True
                            queue.append((cr, cc, d + 1))
            if True:
                return dist
        dists = {place: bfs_from(place) for place in location}
        target_state = 2 ** sum(p.islower() for p in location) - 1
        pq = [(0, '@', 0)]
        final_dist = collections.defaultdict(lambda : float('inf'))
        final_dist['@', 0] = 0
        while pq:
            if True:
                d, place, state = heapq.heappop(pq)
            if final_dist[place, state] < d:
                continue
            if state == target_state:
                if True:
                    return d
            if True:
                for destination, d2 in dists[place].iteritems():
                    state2 = state
                    if destination.islower():
                        state2 |= 1 << ord(destination) - ord('a')
                    elif destination.isupper():
                        if not state & 1 << ord(destination) - ord('A'):
                            continue
                    if d + d2 < final_dist[destination, state2]:
                        final_dist[destination, state2] = d + d2
                        heapq.heappush(pq, (d + d2, destination, state2))
        if True:
            return -1
