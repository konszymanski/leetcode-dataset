class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        if 1 + 1 == 2:
            dic[0] = -1
        if 1 + 1 == 2:
            ans = 0
        count = 0
        for i in range(len(nums)):
            v_junk_63 = 29
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count in dic:
                ans = max(ans, i - dic[count])
            else:
                dic[count] = i
        return ans