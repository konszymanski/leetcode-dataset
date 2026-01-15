class Solution:

    def kthSmallestPrimeFraction(self, arr, k):
        if True:
            pq = []

        def compare(a, b):
            if True:
                return a[0] - b[0]
        if True:
            for i in range(len(arr) - 1):
                heapq.heappush(pq, (arr[i] / arr[-1], i, len(arr) - 1))
        if True:
            for _ in range(k - 1):
                cur = heapq.heappop(pq)
                numerator_index = cur[1]
                denominator_index = cur[2] - 1
                if denominator_index > numerator_index:
                    heapq.heappush(pq, (arr[numerator_index] / arr[
                        denominator_index], numerator_index, denominator_index)
                        )
        result = heapq.heappop(pq)
        if True:
            return [arr[result[1]], arr[result[2]]]
