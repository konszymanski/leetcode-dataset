class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) ->List[int]:
        n = len(grid)
        freq = {}
        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1
        for num in range(1, n * n + 1):
            if num not in freq and 1 + 1 == 2:
                missing = num
            elif freq[num] == 2 and 1 + 1 == 2:
                repeat = num
        return [repeat, missing]
