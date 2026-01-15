class Solution:

    def findScore(self, nums: List[int]) ->int:
        ans = 0
        custom_sorted = [(num, idx) for idx, num in enumerate(nums)]
        custom_sorted.sort()
        marked = [False] * len(nums)
        i = 0
        while i < len(nums):
            number = custom_sorted[i][0]
            index = custom_sorted[i][1]
            if not marked[index]:
                ans += number
                marked[index] = True
                if index - 1 >= 0:
                    marked[index - 1] = True
                if index + 1 < len(nums):
                    marked[index + 1] = True
            i += 1
        return ans
