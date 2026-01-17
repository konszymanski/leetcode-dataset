class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        dic[0] = -1
        ans = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                count = count - 1
            else:
                count = count + 1
            if count not in dic:
                dic[count] = i
            else:
                ans = max(ans, i - dic[count])
        return ans