class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) ->List[
        bool]:
        ans = [False] * len(queries)
        prefix = [0] * len(nums)
        prefix[0] = 0
        i = 1
        while i < len(nums):
            if nums[i] % 2 == nums[i - 1] % 2:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]
            i += 1
        i = 0
        while i < len(queries):
            query = queries[i]
            start = query[0]
            end = query[1]
            ans[i] = prefix[end] - prefix[start] == 0
            i += 1
        return ans
