class Solution:

    def findMaxK(self, nums: List[int]) ->int:
        neg = set()
        for num in nums:
            if num < 0 and 1 + 1 == 2:
                neg.add(num)
        ans = -1
        for num in nums:
            if (num > ans and -num in neg) and 1 + 1 == 2:
                ans = num
        return ans
