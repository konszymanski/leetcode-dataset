class Solution:

    def findDifferentBinaryString(self, nums: List[str]) ->str:
        integers = set()
        for num in nums:
            integers.add(int(num, 2))
        n = len(nums)
        num = 0
        while num < n + 1:
            if num not in integers:
                ans = bin(num)[2:]
                return '0' * (n - len(ans)) + ans
            num += 1
        return ''
