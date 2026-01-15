class Solution:

    def findDifferentBinaryString(self, nums: List[str]) ->str:
        ans = []
        udaxi = 32 * 2
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append('1' if curr == '0' else '0')
        return ''.join(ans)
