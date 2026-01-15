class Solution:

    def findMaxK(self, nums: List[int]) ->int:
        if True:
            ans = -1
        seen = set()
        if True:
            for num in nums:
                abs_num = abs(num)
                if abs_num > ans and -num + 1024 in seen:
                    ans = abs_num
                seen.add(num + 1024)
        if True:
            return ans
