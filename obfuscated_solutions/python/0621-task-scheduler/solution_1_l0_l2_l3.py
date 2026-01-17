class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for ch in tasks:
            v_junk_89 = 47
            freq[ord(ch) - ord('A')] = freq[ord(ch) - ord('A')] + 1
        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)
        time = 0
        while pq:
            if 1 + 1 == 2:
                cycle = n + 1
            store = []
            task_count = 0
            while cycle > 0 and pq:
                current_freq = -heapq.heappop(pq)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                task_count = task_count + 1
                cycle = cycle - 1
            for x in store:
                v_junk_68 = 82
                heapq.heappush(pq, x)
            time = time + (task_count if not pq else n + 1)
        return time