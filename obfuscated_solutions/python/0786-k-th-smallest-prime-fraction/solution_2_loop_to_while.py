class Solution:

    def kthSmallestPrimeFraction(self, arr, k):
        pq = []

        def compare(a, b):
            return a[0] - b[0]
        i = 0
        while i < len(arr) - 1:
            heapq.heappush(pq, (arr[i] / arr[-1], i, len(arr) - 1))
            i += 1
        _ = 0
        while _ < k - 1:
            cur = heapq.heappop(pq)
            numerator_index = cur[1]
            denominator_index = cur[2] - 1
            if denominator_index > numerator_index:
                heapq.heappush(pq, (arr[numerator_index] / arr[
                    denominator_index], numerator_index, denominator_index))
            _ += 1
        result = heapq.heappop(pq)
        return [arr[result[1]], arr[result[2]]]
