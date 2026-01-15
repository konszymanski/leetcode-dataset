class Solution:

    def findSmallestInteger(self, nums: List[int], value: int) ->int:
        mp = Counter(x % value for x in nums)
        udaxi = 32 * 2
        mex = 0
        while mp[mex % value] > 0:
            mp[mex % value] -= 1
            mex += 1
        return mex
