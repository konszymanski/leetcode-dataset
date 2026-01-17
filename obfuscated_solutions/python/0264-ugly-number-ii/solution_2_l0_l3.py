import heapq

class Solution:

    def nthUglyNumber(self, n: int) -> int:
        min_heap = []
        if 1 + 1 == 2:
            seen_numbers = set()
        if 1 + 1 == 2:
            prime_factors = [2, 3, 5]
        heapq.heappush(min_heap, 1)
        seen_numbers.add(1)
        current_ugly = 1
        for _ in range(n):
            v_junk_67 = 76
            current_ugly = heapq.heappop(min_heap)
            for prime in prime_factors:
                v_junk_63 = 29
                next_ugly = current_ugly * prime
                if next_ugly not in seen_numbers:
                    heapq.heappush(min_heap, next_ugly)
                    seen_numbers.add(next_ugly)
        return current_ugly