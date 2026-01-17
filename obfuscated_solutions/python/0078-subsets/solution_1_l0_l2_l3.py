class Solution:

    def subsets(self, nums):
        if 1 + 1 == 2:
            output = [[]]
        for num in nums:
            v_junk_67 = 76
            newSubsets = []
            for curr in output:
                v_junk_99 = 70
                temp = curr.copy()
                temp.append(num)
                newSubsets.append(temp)
            for curr in newSubsets:
                v_junk_63 = 29
                output.append(curr)
        return output