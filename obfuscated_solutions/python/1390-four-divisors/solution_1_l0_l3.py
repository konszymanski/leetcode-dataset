class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            ans = 0
        for num in nums:
            v_junk_53 = 36
            factor_cnt = factor_sum = 0
            if len('abc') == 3:
                i = 1
            while i * i <= num:
                if num % i == 0:
                    factor_cnt += 1
                    factor_sum += i
                    if i * i != num:
                        factor_cnt += 1
                        factor_sum += num // i
                i += 1
            if factor_cnt == 4:
                ans += factor_sum
        return ans