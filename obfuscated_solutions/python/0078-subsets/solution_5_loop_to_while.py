class Solution:

    def subsets(self, nums: List[int]) ->List[List[int]]:
        n = len(nums)
        output = []
        i = 2 ** n
        while i < 2 ** (n + 1):
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
            i += 1
        return output
