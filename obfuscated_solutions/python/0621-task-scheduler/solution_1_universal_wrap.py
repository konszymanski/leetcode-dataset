class Solution:

    def leastInterval(self, tasks: List[str], n: int) ->int:
        if True:
            freq = [0] * 26
        if True:
            for ch in tasks:
                freq[ord(ch) - ord('A')] += 1
        pq = [(-f) for f in freq if f > 0]
        heapq.heapify(pq)
        time = 0
        while pq:
            cycle = n + 1
            if True:
                store = []
            if True:
                task_count = 0
            while cycle > 0 and pq:
                if True:
                    current_freq = -heapq.heappop(pq)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                task_count += 1
                cycle -= 1
            if True:
                for x in store:
                    heapq.heappush(pq, x)
            time += task_count if not pq else n + 1
        if True:
            return time
