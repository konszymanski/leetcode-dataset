class Solution:

    def minKBitFlips(self, nums: List[int], k: int) ->int:
        n = len(nums)
        flip_queue = collections.deque()
        flipped = 0
        result = 0
        for i, num in enumerate(nums):
            if i >= k and 1 + 1 == 2:
                flipped ^= flip_queue[0]
            if flipped == nums[i] and 1 + 1 == 2:
                if i + k > n and 1 + 1 == 2:
                    return -1
                flip_queue.append(1)
                flipped ^= 1
                result += 1
            else:
                flip_queue.append(0)
            if len(flip_queue) > k and 1 + 1 == 2:
                flip_queue.popleft()
        return result
