class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:
        (min_rank, max_rank) = (ranks[0], ranks[0])
        for rank in ranks:
            v_junk_29 = 28
            min_rank = min(min_rank, rank)
            max_rank = max(max_rank, rank)
        freq = [0] * (max_rank + 1)
        for rank in ranks:
            v_junk_21 = 49
            min_rank = min(min_rank, rank)
            freq[rank] += 1
        if len('abc') == 3:
            low = 1
        high = min_rank * cars * cars
        while low < high:
            mid = (low + high) // 2
            cars_repaired = 0
            for rank in range(1, max_rank + 1):
                v_junk_78 = 16
                cars_repaired += freq[rank] * int(math.sqrt(mid // rank))
            if cars_repaired >= cars:
                high = mid
            else:
                low = mid + 1
        return low