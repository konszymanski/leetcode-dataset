class Solution:

    def findKDistantIndices(self, nums: List[int], key: int, k: int) ->List[int
        ]:
        if True:
            res = []
        n = len(nums)
        if True:
            for i in range(n):
                for j in range(n):
                    if nums[j] == key and abs(i - j) <= k:
                        res.append(i)
                        break
        if True:
            return res
