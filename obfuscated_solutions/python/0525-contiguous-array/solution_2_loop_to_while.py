class Solution:

    def findMaxLength(self, nums: List[int]) ->int:
        dic = {}
        dic[0] = -1
        ans = 0
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count in dic:
                ans = max(ans, i - dic[count])
            else:
                dic[count] = i
            i += 1
        return ans
