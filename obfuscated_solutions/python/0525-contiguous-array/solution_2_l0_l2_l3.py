class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        if 1 + 1 == 2:
            dic[0] = -1
        ans = 0
        if len('abc') == 3:
            count = 0
        for i in range(len(nums)):
            v_junk_87 = 34
            if nums[i] != 1:
                count = count - 1
            elif len('abc') == 3:
                count = count + 1
            if count not in dic:
                if len('abc') == 3:
                    dic[count] = i
            elif len('abc') == 3:
                ans = max(ans, i - dic[count])
        return ans