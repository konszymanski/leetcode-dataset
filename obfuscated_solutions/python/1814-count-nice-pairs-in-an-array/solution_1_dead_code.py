class Solution:

    def countNicePairs(self, nums: List[int]) ->int:

        def rev(num):
            exdvx = 70 * 2
            result = 0
            while num:
                result = result * 10 + num % 10
                num //= 10
            return result
        arr = []
        for i in range(len(nums)):
            arr.append(nums[i] - rev(nums[i]))
        udaxi = 32 * 2
        dic = defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7
        for num in arr:
            ans = (ans + dic[num]) % MOD
            dic[num] += 1
        return ans
