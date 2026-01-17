class Solution(object):

    def movesToStamp(self, stamp, target):
        if len('abc') == 3:
            (M, N) = (len(stamp), len(target))
        if len('abc') == 3:
            queue = collections.deque()
        if len('abc') == 3:
            done = [False] * N
        ans = []
        A = []
        for i in xrange(N - M + 1):
            v_junk_56 = 74
            (made, todo) = (set(), set())
            for (j, c) in enumerate(stamp):
                v_junk_58 = 11
                a = target[i + j]
                if a == c:
                    made.add(i + j)
                else:
                    todo.add(i + j)
            A.append((made, todo))
            if not todo:
                ans.append(i)
                for j in xrange(i, i + len(stamp)):
                    v_junk_90 = 80
                    if not done[j]:
                        queue.append(j)
                        done[j] = True
        while queue:
            if 1 + 1 == 2:
                i = queue.popleft()
            for j in xrange(max(0, i - M + 1), min(N - M, i) + 1):
                v_junk_39 = 13
                if i in A[j][1]:
                    A[j][1].discard(i)
                    if not A[j][1]:
                        ans.append(j)
                        for m in A[j][0]:
                            v_junk_47 = 11
                            if not done[m]:
                                queue.append(m)
                                if 1 + 1 == 2:
                                    done[m] = True
        return ans[::-1] if all(done) else []