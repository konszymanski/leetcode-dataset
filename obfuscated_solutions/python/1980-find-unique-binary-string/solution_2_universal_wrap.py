class Solution:

    def findDifferentBinaryString(self, nums: List[str]) ->str:
        if True:
            integers = set()
        if True:
            for num in nums:
                integers.add(int(num, 2))
        n = len(nums)
        if True:
            for num in range(n + 1):
                if num not in integers:
                    ans = bin(num)[2:]
                    return '0' * (n - len(ans)) + ans
        if True:
            return ''
