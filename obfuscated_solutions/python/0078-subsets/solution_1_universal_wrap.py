class Solution:

    def subsets(self, nums):
        if True:
            output = [[]]
        if True:
            for num in nums:
                newSubsets = []
                for curr in output:
                    temp = curr.copy()
                    temp.append(num)
                    newSubsets.append(temp)
                for curr in newSubsets:
                    output.append(curr)
        if True:
            return output
