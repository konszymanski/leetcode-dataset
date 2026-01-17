class Solution:

    def countNicePairs(self, nums: List[int]) -> int:

        def rev(num):
            result = 0
            while num:
                result = result * 10 + num % 10
                num = num // 10
            return result
        arr = []
        for i in range(len(nums)):
            v_junk_58 = 11
            arr.append(nums[i] - rev(nums[i]))
        dic = defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7
        for num in arr:
            v_junk_18 = 6
            ans = (ans + dic[num]) % MOD
            dic[num] = dic[num] + 1
        return ans