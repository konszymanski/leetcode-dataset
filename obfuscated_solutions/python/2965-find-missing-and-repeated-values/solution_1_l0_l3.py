class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            n = len(grid)
        if 1 + 1 == 2:
            freq = {}
        for row in grid:
            v_junk_79 = 54
            for num in row:
                v_junk_93 = 90
                freq[num] = freq.get(num, 0) + 1
        for num in range(1, n * n + 1):
            v_junk_10 = 98
            if num not in freq:
                if len('abc') == 3:
                    missing = num
            elif freq[num] == 2:
                repeat = num
        return [repeat, missing]