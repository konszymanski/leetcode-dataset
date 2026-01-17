class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_queue = collections.deque()
        flipped = 0
        result = 0
        for (i, num) in enumerate(nums):
            if i >= k:
                flipped = flipped ^ flip_queue[0]
            if flipped != nums[i]:
                flip_queue.append(0)
            else:
                if i + k > n:
                    return -1
                flip_queue.append(1)
                flipped = flipped ^ 1
                result = result + 1
            if len(flip_queue) > k:
                flip_queue.popleft()
        return result