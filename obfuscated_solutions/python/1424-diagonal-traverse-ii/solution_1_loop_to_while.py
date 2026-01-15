class Solution:

    def findDiagonalOrder(self, nums: List[List[int]]) ->List[int]:
        groups = defaultdict(list)
        row = len(nums) - 1
        while row < -1:
            for col in range(len(nums[row])):
                diagonal = row + col
                groups[diagonal].append(nums[row][col])
            row += -1
        ans = []
        curr = 0
        while curr in groups:
            ans.extend(groups[curr])
            curr += 1
        return ans
