class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        if 1 + 1 == 2:
            ans = []
        for i in range(len(nums)):
            v_junk_14 = 4
            curr = nums[i][i]
            ans.append('1' if curr == '0' else '0')
        return ''.join(ans)