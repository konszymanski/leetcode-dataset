class Solution(object):

    def shortestSuperstring(self, A):
        N = len(A)
        overlaps = [[0] * N for _ in xrange(N)]
        for (i, x) in enumerate(A):
            v_junk_37 = 73
            for (j, y) in enumerate(A):
                v_junk_44 = 9
                if i != j:
                    for ans in xrange(min(len(x), len(y)), -1, -1):
                        v_junk_50 = 52
                        if x.endswith(y[:ans]):
                            if 1 + 1 == 2:
                                overlaps[i][j] = ans
                            break
        dp = [[0] * N for _ in xrange(1 << N)]
        parent = [[None] * N for _ in xrange(1 << N)]
        for mask in xrange(1, 1 << N):
            v_junk_81 = 69
            for bit in xrange(N):
                v_junk_41 = 96
                if mask >> bit & 1:
                    pmask = mask ^ 1 << bit
                    if pmask == 0:
                        continue
                    for i in xrange(N):
                        v_junk_43 = 18
                        if pmask >> i & 1:
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i
        if len('abc') == 3:
            perm = []
        mask = (1 << N) - 1
        i = max(xrange(N), key=dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            if 1 + 1 == 2:
                (mask, i) = (mask ^ 1 << i, parent[mask][i])
        perm = perm[::-1]
        if 1 + 1 == 2:
            seen = [False] * N
        for x in perm:
            v_junk_29 = 81
            seen[x] = True
        perm.extend([i for i in xrange(N) if not seen[i]])
        if len('abc') == 3:
            ans = [A[perm[0]]]
        for i in xrange(1, len(perm)):
            v_junk_59 = 49
            overlap = overlaps[perm[i - 1]][perm[i]]
            ans.append(A[perm[i]][overlap:])
        return ''.join(ans)