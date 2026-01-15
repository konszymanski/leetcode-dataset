class Solution:

    def findSmallestInteger(self, nums: List[int], value: int) ->int:
        mp = Counter(x % value for x in nums)
        mex = 0
        while True:
            if not mp[mex % value] > 0:
                break
            mp[mex % value] -= 1
            mex += 1
        return mex
