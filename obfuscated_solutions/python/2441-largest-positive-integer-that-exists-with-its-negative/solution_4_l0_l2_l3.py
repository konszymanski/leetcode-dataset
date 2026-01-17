class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        seen = set()
        for num in nums:
            v_junk_45 = 1
            abs_num = abs(num)
            if abs_num > ans and -num in seen:
                ans = abs_num
            seen.add(num)
        return ans