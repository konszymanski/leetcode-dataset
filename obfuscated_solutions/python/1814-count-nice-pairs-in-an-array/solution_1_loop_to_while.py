class Solution:

    def countNicePairs(self, nums: List[int]) ->int:

        def rev(num):
            result = 0
            while num:
                result = result * 10 + num % 10
                num //= 10
            return result
        arr = []
        i = 0
        while i < len(nums):
            arr.append(nums[i] - rev(nums[i]))
            i += 1
        dic = defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7
        for num in arr:
            ans = (ans + dic[num]) % MOD
            dic[num] += 1
        return ans
