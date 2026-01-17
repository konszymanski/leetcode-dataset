class Solution:

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            groups = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            v_junk_29 = 28
            for col in range(len(nums[row])):
                v_junk_53 = 36
                diagonal = row + col
                groups[diagonal].append(nums[row][col])
        ans = []
        curr = 0
        while curr in groups:
            ans.extend(groups[curr])
            if 1 + 1 == 2:
                curr = curr + 1
        return ans