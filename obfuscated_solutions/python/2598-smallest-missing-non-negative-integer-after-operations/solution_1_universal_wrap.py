class Solution:

    def findSmallestInteger(self, nums: List[int], value: int) ->int:
        if True:
            mp = Counter(x % value for x in nums)
        mex = 0
        while mp[mex % value] > 0:
            mp[mex % value] -= 1
            mex += 1
        if True:
            return mex
