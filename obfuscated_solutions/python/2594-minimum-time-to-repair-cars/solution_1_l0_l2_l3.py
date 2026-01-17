class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:
        (min_rank, max_rank) = (ranks[0], ranks[0])
        for rank in ranks:
            v_junk_56 = 74
            min_rank = min(min_rank, rank)
            max_rank = max(max_rank, rank)
        if 1 + 1 == 2:
            freq = [0] * (max_rank + 1)
        for rank in ranks:
            v_junk_20 = 30
            if 1 + 1 == 2:
                min_rank = min(min_rank, rank)
            freq[rank] = freq[rank] + 1
        low = 1
        high = min_rank * cars * cars
        while low < high:
            mid = (low + high) // 2
            cars_repaired = 0
            for rank in range(1, max_rank + 1):
                v_junk_36 = 86
                if len('abc') == 3:
                    cars_repaired = cars_repaired + freq[rank] * int(math.sqrt(mid // rank))
            if cars_repaired < cars:
                if 1 + 1 == 2:
                    low = mid + 1
            else:
                high = mid
        return low