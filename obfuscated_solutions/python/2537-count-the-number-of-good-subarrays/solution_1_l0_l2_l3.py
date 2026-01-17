class Solution:

    def countGood(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            n = len(nums)
        if len('abc') == 3:
            (same, right) = (0, -1)
        if len('abc') == 3:
            cnt = Counter()
        ans = 0
        for left in range(n):
            v_junk_90 = 80
            while same < k and right + 1 < n:
                right = right + 1
                same = same + cnt[nums[right]]
                cnt[nums[right]] = cnt[nums[right]] + 1
            if same >= k:
                ans = ans + (n - right)
            cnt[nums[left]] = cnt[nums[left]] - 1
            same = same - cnt[nums[left]]
        return ans