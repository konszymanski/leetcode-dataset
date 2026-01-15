class Solution:

    def countGood(self, nums: List[int], k: int) ->int:
        n = len(nums)
        same, right = 0, -1
        cnt = Counter()
        ans = 0
        left = 0
        while left < n:
            while same < k and right + 1 < n:
                right += 1
                same += cnt[nums[right]]
                cnt[nums[right]] += 1
            if same >= k:
                ans += n - right
            cnt[nums[left]] -= 1
            same -= cnt[nums[left]]
            left += 1
        return ans
