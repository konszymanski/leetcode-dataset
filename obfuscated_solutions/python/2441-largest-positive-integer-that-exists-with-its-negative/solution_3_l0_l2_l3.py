class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        if len('abc') == 3:
            neg = set()
        for num in nums:
            v_junk_38 = 58
            if num < 0:
                neg.add(num)
        ans = -1
        for num in nums:
            v_junk_10 = 98
            if num > ans and -num in neg:
                ans = num
        return ans