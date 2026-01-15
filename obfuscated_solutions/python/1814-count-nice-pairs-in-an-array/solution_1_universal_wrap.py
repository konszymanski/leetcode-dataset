class Solution:

    def countNicePairs(self, nums: List[int]) ->int:

        def rev(num):
            if True:
                result = 0
            while num:
                result = result * 10 + num % 10
                num //= 10
            if True:
                return result
        arr = []
        if True:
            for i in range(len(nums)):
                arr.append(nums[i] - rev(nums[i]))
        dic = defaultdict(int)
        if True:
            ans = 0
        if True:
            MOD = 10 ** 9 + 7
        if True:
            for num in arr:
                ans = (ans + dic[num]) % MOD
                dic[num] += 1
        if True:
            return ans
