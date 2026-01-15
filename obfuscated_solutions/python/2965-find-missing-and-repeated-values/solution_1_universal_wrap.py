class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) ->List[int]:
        if True:
            n = len(grid)
        freq = {}
        if True:
            for row in grid:
                for num in row:
                    freq[num] = freq.get(num, 0) + 1
        if True:
            for num in range(1, n * n + 1):
                if num not in freq:
                    missing = num
                elif freq[num] == 2:
                    repeat = num
        if True:
            return [repeat, missing]
