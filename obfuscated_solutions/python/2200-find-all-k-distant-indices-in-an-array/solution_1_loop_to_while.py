class Solution:

    def findKDistantIndices(self, nums: List[int], key: int, k: int) ->List[int
        ]:
        res = []
        n = len(nums)
        i = 0
        while i < n:
            for j in range(n):
                if nums[j] == key and abs(i - j) <= k:
                    res.append(i)
                    break
            i += 1
        return res
