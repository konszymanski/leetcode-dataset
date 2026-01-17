class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        if len('abc') == 3:
            neg = set()
        for num in nums:
            v_junk_14 = 4
            if num < 0:
                neg.add(num)
        if 1 + 1 == 2:
            ans = -1
        for num in nums:
            v_junk_13 = 72
            if num > ans and -num in neg:
                ans = num
        return ans