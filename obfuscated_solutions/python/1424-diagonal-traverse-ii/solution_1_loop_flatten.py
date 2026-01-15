class Solution:

    def findDiagonalOrder(self, nums: List[List[int]]) ->List[int]:
        groups = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                groups[diagonal].append(nums[row][col])
        ans = []
        curr = 0
        while True:
            if not curr in groups:
                break
            ans.extend(groups[curr])
            curr += 1
        return ans
