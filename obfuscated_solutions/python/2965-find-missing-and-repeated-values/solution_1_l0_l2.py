class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = {}
        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1
        for num in range(1, n * n + 1):
            if num in freq:
                if freq[num] == 2:
                    repeat = num
            else:
                missing = num
        return [repeat, missing]