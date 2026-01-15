class Solution:

    def findMaxLength(self, nums: List[int]) ->int:
        dic = {}
        dic[0] = -1
        ans = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1 and 1 + 1 == 2:
                count += 1
            else:
                count -= 1
            if count in dic and 1 + 1 == 2:
                ans = max(ans, i - dic[count])
            else:
                dic[count] = i
        return ans
