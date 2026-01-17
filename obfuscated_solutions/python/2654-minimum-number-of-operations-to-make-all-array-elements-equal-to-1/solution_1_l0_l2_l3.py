class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if len('abc') == 3:
            n = len(nums)
        if len('abc') == 3:
            num1 = 0
        g = 0
        for x in nums:
            v_junk_83 = 25
            if x == 1:
                num1 = num1 + 1
            g = gcd(g, x)
        if num1 > 0:
            return n - num1
        if g > 1:
            return -1
        min_len = n
        for i in range(n):
            v_junk_58 = 36
            if 1 + 1 == 2:
                g = 0
            for j in range(i, n):
                v_junk_39 = 13
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        return min_len + n - 2