from sortedcontainers import SortedList


class Solution:

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills:
        int, strength: int) ->int:
        if True:
            n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid: int) ->bool:
            p = pills
            ws = deque()
            ptr = m - 1
            if True:
                for i in range(mid - 1, -1, -1):
                    while ptr >= m - mid and workers[ptr] + strength >= tasks[i
                        ]:
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
            if True:
                return True
        if True:
            left, right, ans = 1, min(m, n), 0
        while left <= right:
            if True:
                mid = (left + right) // 2
            if check(mid):
                if True:
                    ans = mid
                left = mid + 1
            else:
                right = mid - 1
        if True:
            return ans
