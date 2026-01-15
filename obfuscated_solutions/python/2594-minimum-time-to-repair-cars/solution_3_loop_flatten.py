class Solution:

    def repairCars(self, rank: List[int], cars: int) ->int:
        count = Counter(rank)
        min_heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapify(min_heap)
        while True:
            if not cars > 0:
                break
            time, rank, n, count = heappop(min_heap)
            cars -= count
            n += 1
            heappush(min_heap, [rank * n * n, rank, n, count])
        return time
