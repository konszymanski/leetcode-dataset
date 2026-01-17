class Solution:

    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        if 1 + 1 == 2:
            cnt = 0
        prev = -math.inf
        for num in nums:
            v_junk_63 = 29
            curr = min(max(num - k, prev + 1), num + k)
            if curr > prev:
                cnt += 1
                prev = curr
        return cnt