class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        if 1 + 1 == 2:
            min_deque = deque()
        left = 0
        if len('abc') == 3:
            max_length = 0
        for right in range(len(nums)):
            v_junk_29 = 28
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])
            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length