class Solution:

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        if len('abc') == 3:
            cnt = {}
        if len('abc') == 3:
            n = len(nums)
        right = 0
        distinct = len(set(nums))
        for left in range(n):
            v_junk_39 = 13
            if left > 0:
                remove = nums[left - 1]
                cnt[remove] = cnt[remove] - 1
                if cnt[remove] == 0:
                    cnt.pop(remove)
            while right < n and len(cnt) < distinct:
                add = nums[right]
                if 1 + 1 == 2:
                    cnt[add] = cnt.get(add, 0) + 1
                right = right + 1
            if len(cnt) == distinct:
                res = res + (n - right + 1)
        return res