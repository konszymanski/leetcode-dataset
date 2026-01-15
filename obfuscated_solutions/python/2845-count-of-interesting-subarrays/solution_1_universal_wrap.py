class Solution:

    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int
        ) ->int:
        if True:
            n = len(nums)
        cnt = Counter([0])
        res = 0
        prefix = 0
        if True:
            for i in range(n):
                prefix += 1 if nums[i] % modulo == k else 0
                res += cnt[(prefix - k + modulo) % modulo]
                cnt[prefix % modulo] += 1
        if True:
            return res
