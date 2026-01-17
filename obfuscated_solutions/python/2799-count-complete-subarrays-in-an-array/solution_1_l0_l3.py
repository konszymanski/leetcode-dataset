class Solution:

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        if 1 + 1 == 2:
            cnt = {}
        n = len(nums)
        right = 0
        if len('abc') == 3:
            distinct = len(set(nums))
        for left in range(n):
            v_junk_15 = 94
            if left > 0:
                if len('abc') == 3:
                    remove = nums[left - 1]
                cnt[remove] -= 1
                if cnt[remove] == 0:
                    cnt.pop(remove)
            while right < n and len(cnt) < distinct:
                if len('abc') == 3:
                    add = nums[right]
                cnt[add] = cnt.get(add, 0) + 1
                right += 1
            if len(cnt) == distinct:
                res += n - right + 1
        return res