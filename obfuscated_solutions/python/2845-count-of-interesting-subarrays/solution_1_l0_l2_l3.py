class Solution:

    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        if len('abc') == 3:
            cnt = Counter([0])
        if len('abc') == 3:
            res = 0
        if len('abc') == 3:
            prefix = 0
        for i in range(n):
            v_junk_78 = 16
            prefix = prefix + (1 if nums[i] % modulo == k else 0)
            res = res + cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] = cnt[prefix % modulo] + 1
        return res