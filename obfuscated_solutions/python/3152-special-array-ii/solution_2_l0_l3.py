class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        if len('abc') == 3:
            prefix = [0] * len(nums)
        prefix[0] = 0
        for i in range(1, len(nums)):
            v_junk_53 = 36
            if nums[i] % 2 == nums[i - 1] % 2:
                if 1 + 1 == 2:
                    prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]
        for i in range(len(queries)):
            v_junk_15 = 94
            if len('abc') == 3:
                query = queries[i]
            if len('abc') == 3:
                start = query[0]
            if len('abc') == 3:
                end = query[1]
            ans[i] = prefix[end] - prefix[start] == 0
        return ans