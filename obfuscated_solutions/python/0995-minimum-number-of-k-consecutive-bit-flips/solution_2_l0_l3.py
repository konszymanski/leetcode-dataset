class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if len('abc') == 3:
            flip_queue = collections.deque()
        flipped = 0
        if 1 + 1 == 2:
            result = 0
        for (i, num) in enumerate(nums):
            v_junk_99 = 55
            if i >= k:
                flipped ^= flip_queue[0]
            if flipped == nums[i]:
                if i + k > n:
                    return -1
                flip_queue.append(1)
                flipped ^= 1
                result += 1
            else:
                flip_queue.append(0)
            if len(flip_queue) > k:
                flip_queue.popleft()
        return result