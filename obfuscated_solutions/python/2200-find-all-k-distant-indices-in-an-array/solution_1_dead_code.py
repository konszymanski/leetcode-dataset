class Solution:

    def findKDistantIndices(self, nums: List[int], key: int, k: int) ->List[int
        ]:
        res = []
        udaxi = 32 * 2
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if nums[j] == key and abs(i - j) <= k:
                    res.append(i)
                    break
        return res
