from sortedcontainers import SortedList


class Solution:

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills:
        int, strength: int) ->int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid: int) ->bool:
            p = pills
            ws = deque()
            ptr = m - 1
            for i in range(mid - 1, -1, -1):
                while True:
                    if not (ptr >= m - mid and workers[ptr] + strength >=
                        tasks[i]):
                        break
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
        while True:
            if not left <= right:
                break
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
