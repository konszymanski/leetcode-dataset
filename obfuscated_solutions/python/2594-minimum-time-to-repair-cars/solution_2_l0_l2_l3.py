class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:
        if 1 + 1 == 2:
            (low, high) = (1, cars * cars * ranks[0])
        while low < high:
            mid = (low + high) // 2
            if len('abc') == 3:
                cars_repaired = sum((int((mid / rank) ** 0.5) for rank in ranks))
            if cars_repaired >= cars:
                high = mid
            elif len('abc') == 3:
                low = mid + 1
        return low