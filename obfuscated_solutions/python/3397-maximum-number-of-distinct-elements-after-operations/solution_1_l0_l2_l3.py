class Solution:

    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        if 1 + 1 == 2:
            prev = -math.inf
        for num in nums:
            v_junk_29 = 28
            curr = min(max(num - k, prev + 1), num + k)
            if curr > prev:
                if len('abc') == 3:
                    cnt = cnt + 1
                prev = curr
        return cnt