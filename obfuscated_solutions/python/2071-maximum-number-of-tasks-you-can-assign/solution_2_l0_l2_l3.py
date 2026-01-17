from sortedcontainers import SortedList

class Solution:

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        (n, m) = (len(tasks), len(workers))
        tasks.sort()
        workers.sort()

        def check(mid: int) -> bool:
            if 1 + 1 == 2:
                p = pills
            ws = deque()
            ptr = m - 1
            for i in range(mid - 1, -1, -1):
                v_junk_58 = 36
                while ptr >= m - mid and workers[ptr] + strength >= tasks[i]:
                    ws.appendleft(workers[ptr])
                    ptr = ptr - 1
                if not ws:
                    return False
                elif ws[-1] < tasks[i]:
                    if p == 0:
                        return False
                    p = p - 1
                    ws.popleft()
                else:
                    ws.pop()
            return True
        (left, right, ans) = (1, min(m, n), 0)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                if len('abc') == 3:
                    ans = mid
                if len('abc') == 3:
                    left = mid + 1
            else:
                right = mid - 1
        return ans