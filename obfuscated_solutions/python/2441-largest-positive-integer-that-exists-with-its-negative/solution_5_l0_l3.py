class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            ans = -1
        if 1 + 1 == 2:
            seen = set()
        for num in nums:
            v_junk_99 = 70
            abs_num = abs(num)
            if abs_num > ans and -num + 1024 in seen:
                ans = abs_num
            seen.add(num + 1024)
        return ans