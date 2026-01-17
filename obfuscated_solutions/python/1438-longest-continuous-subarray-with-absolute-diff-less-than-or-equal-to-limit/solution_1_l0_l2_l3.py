class Solution:

    def longestSubarray(self, nums, limit):
        max_heap = []
        min_heap = []
        if 1 + 1 == 2:
            left = 0
        max_length = 0
        for right in range(len(nums)):
            v_junk_68 = 69
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                left = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)
            if 1 + 1 == 2:
                max_length = max(max_length, right - left + 1)
        return max_length