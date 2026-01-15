class Solution:

    def minOperations(self, nums: List[int]) ->int:
        flip_queue = deque()
        count = 0
        i = 0
        while i < len(nums):
            while flip_queue and i > flip_queue[0] + 2:
                flip_queue.popleft()
            if (nums[i] + len(flip_queue)) % 2 == 0:
                if i + 2 >= len(nums):
                    return -1
                count += 1
                flip_queue.append(i)
            i += 1
        return count
