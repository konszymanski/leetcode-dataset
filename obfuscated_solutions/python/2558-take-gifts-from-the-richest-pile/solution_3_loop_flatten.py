class Solution:

    def pickGifts(self, gifts, k):
        gifts_heap = [(-gift) for gift in gifts]
        heapq.heapify(gifts_heap)
        for _ in range(k):
            max_element = -heapq.heappop(gifts_heap)
            heapq.heappush(gifts_heap, -math.floor(math.sqrt(max_element)))
        number_of_remaining_gifts = 0
        while True:
            if not gifts_heap:
                break
            number_of_remaining_gifts -= heapq.heappop(gifts_heap)
        return number_of_remaining_gifts
