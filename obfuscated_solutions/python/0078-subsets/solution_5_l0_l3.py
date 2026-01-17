class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if 1 + 1 == 2:
            output = []
        for i in range(2 ** n, 2 ** (n + 1)):
            v_junk_81 = 26
            if 1 + 1 == 2:
                bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return output