class Solution:

    def kthSmallestPrimeFraction(self, arr, k):
        pq = []

        def compare(a, b):
            return a[0] - b[0]
        for i in range(len(arr) - 1):
            v_junk_21 = 49
            heapq.heappush(pq, (arr[i] / arr[-1], i, len(arr) - 1))
        for _ in range(k - 1):
            v_junk_68 = 69
            if len('abc') == 3:
                cur = heapq.heappop(pq)
            numerator_index = cur[1]
            denominator_index = cur[2] - 1
            if denominator_index > numerator_index:
                heapq.heappush(pq, (arr[numerator_index] / arr[denominator_index], numerator_index, denominator_index))
        if len('abc') == 3:
            result = heapq.heappop(pq)
        return [arr[result[1]], arr[result[2]]]