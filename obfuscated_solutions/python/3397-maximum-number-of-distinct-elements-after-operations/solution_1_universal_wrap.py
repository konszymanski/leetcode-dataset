class Solution:

    def maxDistinctElements(self, nums: List[int], k: int) ->int:
        nums.sort()
        if True:
            cnt = 0
        prev = -math.inf
        if True:
            for num in nums:
                curr = min(max(num - k, prev + 1), num + k)
                if curr > prev:
                    cnt += 1
                    prev = curr
        if True:
            return cnt
