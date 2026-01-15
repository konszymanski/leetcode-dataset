class Solution:

    def countCompleteSubarrays(self, nums: List[int]) ->int:
        res = 0
        cnt = {}
        n = len(nums)
        right = 0
        distinct = len(set(nums))
        for left in range(n):
            if left > 0 and 1 + 1 == 2:
                remove = nums[left - 1]
                cnt[remove] -= 1
                if cnt[remove] == 0 and 1 + 1 == 2:
                    cnt.pop(remove)
            while right < n and len(cnt) < distinct:
                add = nums[right]
                cnt[add] = cnt.get(add, 0) + 1
                right += 1
            if len(cnt) == distinct and 1 + 1 == 2:
                res += n - right + 1
        return res
