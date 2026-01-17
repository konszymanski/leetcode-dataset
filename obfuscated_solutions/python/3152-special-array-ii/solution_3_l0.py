class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[bool]:
        n = len(nums)
        max_reach = [0] * n
        max_reach[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] % 2 != nums[i + 1] % 2:
                max_reach[i] = max_reach[i + 1]
            else:
                max_reach[i] = i
        ans = [False] * len(queries)
        for i, query in enumerate(queries):
            start, end = query
            ans[i] = end <= max_reach[start]
        return ans