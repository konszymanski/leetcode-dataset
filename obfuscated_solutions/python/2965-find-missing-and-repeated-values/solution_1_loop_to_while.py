class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) ->List[int]:
        n = len(grid)
        freq = {}
        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1
        num = 1
        while num < n * n + 1:
            if num not in freq:
                missing = num
            elif freq[num] == 2:
                repeat = num
            num += 1
        return [repeat, missing]
