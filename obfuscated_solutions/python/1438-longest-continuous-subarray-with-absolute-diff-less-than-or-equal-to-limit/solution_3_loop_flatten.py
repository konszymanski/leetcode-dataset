class Solution:

    def longestSubarray(self, nums: List[int], limit: int) ->int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0
        for right in range(len(nums)):
            while True:
                if not (max_deque and max_deque[-1] < nums[right]):
                    break
                max_deque.pop()
            max_deque.append(nums[right])
            while True:
                if not (min_deque and min_deque[-1] > nums[right]):
                    break
                min_deque.pop()
            min_deque.append(nums[right])
            while True:
                if not max_deque[0] - min_deque[0] > limit:
                    break
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
