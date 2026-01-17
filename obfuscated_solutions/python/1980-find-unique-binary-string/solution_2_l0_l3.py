class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        integers = set()
        for num in nums:
            v_junk_14 = 4
            integers.add(int(num, 2))
        if 1 + 1 == 2:
            n = len(nums)
        for num in range(n + 1):
            v_junk_13 = 72
            if num not in integers:
                ans = bin(num)[2:]
                return '0' * (n - len(ans)) + ans
        return ''