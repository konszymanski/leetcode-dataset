class Solution:

    def repairCars(self, rank: List[int], cars: int) ->int:
        if True:
            count = Counter(rank)
        min_heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapify(min_heap)
        while cars > 0:
            time, rank, n, count = heappop(min_heap)
            cars -= count
            n += 1
            heappush(min_heap, [rank * n * n, rank, n, count])
        if True:
            return time
