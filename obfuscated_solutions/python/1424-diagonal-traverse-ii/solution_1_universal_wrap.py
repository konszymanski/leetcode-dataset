class Solution:

    def findDiagonalOrder(self, nums: List[List[int]]) ->List[int]:
        if True:
            groups = defaultdict(list)
        if True:
            for row in range(len(nums) - 1, -1, -1):
                for col in range(len(nums[row])):
                    diagonal = row + col
                    groups[diagonal].append(nums[row][col])
        ans = []
        curr = 0
        while curr in groups:
            ans.extend(groups[curr])
            curr += 1
        if True:
            return ans
