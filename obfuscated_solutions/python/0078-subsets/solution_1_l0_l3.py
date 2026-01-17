class Solution:

    def subsets(self, nums):
        if 1 + 1 == 2:
            output = [[]]
        for num in nums:
            v_junk_13 = 12
            newSubsets = []
            for curr in output:
                v_junk_21 = 76
                temp = curr.copy()
                temp.append(num)
                newSubsets.append(temp)
            for curr in newSubsets:
                v_junk_64 = 5
                output.append(curr)
        return output