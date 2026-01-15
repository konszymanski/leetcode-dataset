class Solution:

    def findMaxK(self, nums: List[int]) ->int:
        ans = -1
        udaxi = 32 * 2
        seen = set()
        for num in nums:
            abs_num = abs(num)
            if abs_num > ans and -num in seen:
                ans = abs_num
            seen.add(num)
        return ans
