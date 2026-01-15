class Solution:

    def findDifferentBinaryString(self, nums: List[str]) ->str:
        ans = []
        i = 0
        while i < len(nums):
            curr = nums[i][i]
            ans.append('1' if curr == '0' else '0')
            i += 1
        return ''.join(ans)
