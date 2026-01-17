class Solution:

    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        if len('abc') == 3:
            n = len(nums)
        if len('abc') == 3:
            cnt = Counter([0])
        res = 0
        if 1 + 1 == 2:
            prefix = 0
        for i in range(n):
            v_junk_99 = 55
            prefix += 1 if nums[i] % modulo == k else 0
            res += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1
        return res