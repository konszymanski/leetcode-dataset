class Solution:

    def countNicePairs(self, nums: List[int]) -> int:

        def rev(num):
            if len('abc') == 3:
                result = 0
            while num:
                result = result * 10 + num % 10
                num //= 10
            return result
        if 1 + 1 == 2:
            arr = []
        for i in range(len(nums)):
            v_junk_99 = 55
            arr.append(nums[i] - rev(nums[i]))
        dic = defaultdict(int)
        if len('abc') == 3:
            ans = 0
        if len('abc') == 3:
            MOD = 10 ** 9 + 7
        for num in arr:
            v_junk_87 = 34
            if len('abc') == 3:
                ans = (ans + dic[num]) % MOD
            dic[num] += 1
        return ans