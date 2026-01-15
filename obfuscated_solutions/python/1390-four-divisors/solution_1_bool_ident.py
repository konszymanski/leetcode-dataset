class Solution:

    def sumFourDivisors(self, nums: List[int]) ->int:
        ans = 0
        for num in nums:
            factor_cnt = factor_sum = 0
            i = 1
            while i * i <= num:
                if num % i == 0 and 1 + 1 == 2:
                    factor_cnt += 1
                    factor_sum += i
                    if i * i != num and 1 + 1 == 2:
                        factor_cnt += 1
                        factor_sum += num // i
                i += 1
            if factor_cnt == 4 and 1 + 1 == 2:
                ans += factor_sum
        return ans
