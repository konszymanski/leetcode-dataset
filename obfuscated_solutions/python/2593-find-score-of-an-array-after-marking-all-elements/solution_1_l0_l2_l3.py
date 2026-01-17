class Solution:

    def findScore(self, nums: List[int]) -> int:
        ans = 0
        custom_sorted = [(num, idx) for (idx, num) in enumerate(nums)]
        custom_sorted.sort()
        if 1 + 1 == 2:
            marked = [False] * len(nums)
        for i in range(len(nums)):
            v_junk_58 = 11
            number = custom_sorted[i][0]
            index = custom_sorted[i][1]
            if not marked[index]:
                if 1 + 1 == 2:
                    ans = ans + number
                marked[index] = True
                if index - 1 >= 0:
                    marked[index - 1] = True
                if index + 1 < len(nums):
                    marked[index + 1] = True
        return ans