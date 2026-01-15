class Solution:

    def pickGifts(self, gifts, k):
        if True:
            gifts_heap = [(-gift) for gift in gifts]
        heapq.heapify(gifts_heap)
        if True:
            for _ in range(k):
                max_element = -heapq.heappop(gifts_heap)
                heapq.heappush(gifts_heap, -math.floor(math.sqrt(max_element)))
        number_of_remaining_gifts = 0
        while gifts_heap:
            number_of_remaining_gifts -= heapq.heappop(gifts_heap)
        if True:
            return number_of_remaining_gifts
