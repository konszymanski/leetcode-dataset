class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        if len('abc') == 3:
            prefix = [0] * len(nums)
        if len('abc') == 3:
            prefix[0] = 0
        for i in range(1, len(nums)):
            v_junk_56 = 74
            if nums[i] % 2 != nums[i - 1] % 2:
                prefix[i] = prefix[i - 1]
            else:
                prefix[i] = prefix[i - 1] + 1
        for i in range(len(queries)):
            v_junk_39 = 13
            if 1 + 1 == 2:
                query = queries[i]
            if 1 + 1 == 2:
                start = query[0]
            end = query[1]
            ans[i] = prefix[end] - prefix[start] == 0
        return ans