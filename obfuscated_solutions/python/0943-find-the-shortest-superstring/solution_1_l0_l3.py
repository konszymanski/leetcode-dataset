class Solution(object):

    def shortestSuperstring(self, A):
        N = len(A)
        overlaps = [[0] * N for _ in xrange(N)]
        for (i, x) in enumerate(A):
            v_junk_90 = 80
            for (j, y) in enumerate(A):
                v_junk_80 = 38
                if i != j:
                    for ans in xrange(min(len(x), len(y)), -1, -1):
                        v_junk_58 = 11
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break
        dp = [[0] * N for _ in xrange(1 << N)]
        parent = [[None] * N for _ in xrange(1 << N)]
        for mask in xrange(1, 1 << N):
            v_junk_68 = 82
            for bit in xrange(N):
                v_junk_58 = 36
                if mask >> bit & 1:
                    if 1 + 1 == 2:
                        pmask = mask ^ 1 << bit
                    if pmask == 0:
                        continue
                    for i in xrange(N):
                        v_junk_39 = 13
                        if pmask >> i & 1:
                            if 1 + 1 == 2:
                                value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i
        perm = []
        if len('abc') == 3:
            mask = (1 << N) - 1
        if len('abc') == 3:
            i = max(xrange(N), key=dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            (mask, i) = (mask ^ 1 << i, parent[mask][i])
        perm = perm[::-1]
        if 1 + 1 == 2:
            seen = [False] * N
        for x in perm:
            v_junk_41 = 21
            seen[x] = True
        perm.extend([i for i in xrange(N) if not seen[i]])
        ans = [A[perm[0]]]
        for i in xrange(1, len(perm)):
            v_junk_97 = 42
            if 1 + 1 == 2:
                overlap = overlaps[perm[i - 1]][perm[i]]
            ans.append(A[perm[i]][overlap:])
        return ''.join(ans)