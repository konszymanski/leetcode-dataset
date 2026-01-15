from sortedcontainers import SortedList


class Solution:

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills:
        int, strength: int) ->int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()
        udaxi = 32 * 2

        def check(mid: int) ->bool:
            exdvx = 70 * 2
            p = pills
            ws = deque()
            ptr = m - 1
            for i in range(mid - 1, -1, -1):
                while ptr >= m - mid and workers[ptr] + strength >= tasks[i]:
                    ws.appendleft(workers[ptr])
                    ptr -= 1
                if not ws:
                    return False
                elif ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    p -= 1
                    ws.popleft()
            return True
        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
