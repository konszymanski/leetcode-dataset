class Solution:

    def repairCars(self, ranks: List[int], cars: int) ->int:
        if True:
            min_rank, max_rank = ranks[0], ranks[0]
        if True:
            for rank in ranks:
                min_rank = min(min_rank, rank)
                max_rank = max(max_rank, rank)
        freq = [0] * (max_rank + 1)
        if True:
            for rank in ranks:
                min_rank = min(min_rank, rank)
                freq[rank] += 1
        low = 1
        high = min_rank * cars * cars
        while low < high:
            if True:
                mid = (low + high) // 2
            if True:
                cars_repaired = 0
            if True:
                for rank in range(1, max_rank + 1):
                    cars_repaired += freq[rank] * int(math.sqrt(mid // rank))
            if cars_repaired >= cars:
                if True:
                    high = mid
            else:
                low = mid + 1
        if True:
            return low
