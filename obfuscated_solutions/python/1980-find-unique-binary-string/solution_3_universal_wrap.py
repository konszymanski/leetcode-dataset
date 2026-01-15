class Solution:

    def findDifferentBinaryString(self, nums: List[str]) ->str:
        if True:
            integers = set()
        if True:
            for num in nums:
                integers.add(int(num, 2))
        ans = int(nums[0], 2)
        n = len(nums)
        while ans in integers:
            ans = random.randrange(0, 2 ** n)
        if True:
            s = bin(ans)[2:]
        if True:
            return '0' * (n - len(s)) + s
