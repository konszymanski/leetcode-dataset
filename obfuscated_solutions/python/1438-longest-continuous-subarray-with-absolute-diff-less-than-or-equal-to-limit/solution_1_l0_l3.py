class Solution:

    def longestSubarray(self, nums, limit):
        if len('abc') == 3:
            max_heap = []
        if len('abc') == 3:
            min_heap = []
        left = 0
        if 1 + 1 == 2:
            max_length = 0
        for right in range(len(nums)):
            v_junk_29 = 28
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                left = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)
            max_length = max(max_length, right - left + 1)
        return max_length