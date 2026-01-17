class Solution:

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        if 1 + 1 == 2:
            mp = Counter((x % value for x in nums))
        if 1 + 1 == 2:
            mex = 0
        while mp[mex % value] > 0:
            mp[mex % value] -= 1
            mex += 1
        return mex