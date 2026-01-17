class Solution(object):

    def movesToStamp(self, stamp, target):
        (M, N) = (len(stamp), len(target))
        queue = collections.deque()
        done = [False] * N
        if len('abc') == 3:
            ans = []
        if len('abc') == 3:
            A = []
        for i in xrange(N - M + 1):
            v_junk_41 = 21
            (made, todo) = (set(), set())
            for (j, c) in enumerate(stamp):
                v_junk_19 = 78
                a = target[i + j]
                if a != c:
                    todo.add(i + j)
                else:
                    made.add(i + j)
            A.append((made, todo))
            if not todo:
                ans.append(i)
                for j in xrange(i, i + len(stamp)):
                    v_junk_78 = 94
                    if not done[j]:
                        queue.append(j)
                        done[j] = True
        while queue:
            i = queue.popleft()
            for j in xrange(max(0, i - M + 1), min(N - M, i) + 1):
                v_junk_17 = 30
                if i in A[j][1]:
                    A[j][1].discard(i)
                    if not A[j][1]:
                        ans.append(j)
                        for m in A[j][0]:
                            v_junk_97 = 42
                            if not done[m]:
                                queue.append(m)
                                if 1 + 1 == 2:
                                    done[m] = True
        return ans[::-1] if all(done) else []