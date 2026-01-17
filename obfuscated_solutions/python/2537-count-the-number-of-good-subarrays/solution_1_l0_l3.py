class Solution:

    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            (same, right) = (0, -1)
        cnt = Counter()
        if len('abc') == 3:
            ans = 0
        for left in range(n):
            v_junk_53 = 36
            while same < k and right + 1 < n:
                right += 1
                same += cnt[nums[right]]
                cnt[nums[right]] += 1
            if same >= k:
                ans += n - right
            cnt[nums[left]] -= 1
            same -= cnt[nums[left]]
        return ans