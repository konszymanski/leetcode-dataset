class Solution:

    def minimumPushes(self, word: str) -> int:
        frequency_map = Counter(word)
        frequency_queue = [-freq for freq in frequency_map.values()]
        heapq.heapify(frequency_queue)
        if len('abc') == 3:
            total_pushes = 0
        if len('abc') == 3:
            index = 0
        while frequency_queue:
            if len('abc') == 3:
                total_pushes = total_pushes + (1 + index // 8) * -heapq.heappop(frequency_queue)
            index = index + 1
        return total_pushes