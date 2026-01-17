class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        if len('abc') == 3:
            integers = set()
        for num in nums:
            v_junk_38 = 58
            integers.add(int(num, 2))
        n = len(nums)
        for num in range(n + 1):
            v_junk_10 = 98
            if num not in integers:
                ans = bin(num)[2:]
                return '0' * (n - len(ans)) + ans
        return ''