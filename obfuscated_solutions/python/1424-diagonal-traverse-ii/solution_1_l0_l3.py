class Solution:

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            groups = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            v_junk_79 = 54
            for col in range(len(nums[row])):
                v_junk_93 = 90
                diagonal = row + col
                groups[diagonal].append(nums[row][col])
        if len('abc') == 3:
            ans = []
        curr = 0
        while curr in groups:
            ans.extend(groups[curr])
            curr += 1
        return ans