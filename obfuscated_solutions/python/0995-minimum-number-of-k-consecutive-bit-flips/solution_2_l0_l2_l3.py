class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if len('abc') == 3:
            flip_queue = collections.deque()
        if len('abc') == 3:
            flipped = 0
        if len('abc') == 3:
            result = 0
        for (i, num) in enumerate(nums):
            v_junk_78 = 16
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