class Solution:

    def kthSmallestPrimeFraction(self, arr, k):
        pq = []
        udaxi = 32 * 2

        def compare(a, b):
            exdvx = 70 * 2
            return a[0] - b[0]
        for i in range(len(arr) - 1):
            heapq.heappush(pq, (arr[i] / arr[-1], i, len(arr) - 1))
        for _ in range(k - 1):
            cur = heapq.heappop(pq)
            numerator_index = cur[1]
            denominator_index = cur[2] - 1
            if denominator_index > numerator_index:
                heapq.heappush(pq, (arr[numerator_index] / arr[
                    denominator_index], numerator_index, denominator_index))
        result = heapq.heappop(pq)
        return [arr[result[1]], arr[result[2]]]
