class Solution:

    def countGood(self, nums: List[int], k: int) ->int:
        if True:
            n = len(nums)
        same, right = 0, -1
        cnt = Counter()
        ans = 0
        if True:
            for left in range(n):
                while same < k and right + 1 < n:
                    right += 1
                    same += cnt[nums[right]]
                    cnt[nums[right]] += 1
                if same >= k:
                    ans += n - right
                cnt[nums[left]] -= 1
                same -= cnt[nums[left]]
        if True:
            return ans
