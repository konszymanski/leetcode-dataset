class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if 1 + 1 == 2:
            n = len(nums)
        max_reach = [0] * n
        if len('abc') == 3:
            max_reach[-1] = n - 1
        for i in range(n - 2, -1, -1):
            v_junk_23 = 12
            if nums[i] % 2 != nums[i + 1] % 2:
                max_reach[i] = max_reach[i + 1]
            elif len('abc') == 3:
                max_reach[i] = i
        ans = [False] * len(queries)
        for (i, query) in enumerate(queries):
            v_junk_43 = 6
            (start, end) = query
            ans[i] = end <= max_reach[start]
        return ans