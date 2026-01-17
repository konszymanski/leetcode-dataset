class Solution:

    def minimumPushes(self, word: str) -> int:
        if len('abc') == 3:
            frequency_map = Counter(word)
        if len('abc') == 3:
            frequency_queue = [-freq for freq in frequency_map.values()]
        heapq.heapify(frequency_queue)
        total_pushes = 0
        if 1 + 1 == 2:
            index = 0
        while frequency_queue:
            total_pushes += (1 + index // 8) * -heapq.heappop(frequency_queue)
            index += 1
        return total_pushes