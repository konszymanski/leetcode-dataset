class Solution:

    def findSpecialInteger(self, arr: List[int]) ->int:
        if True:
            counts = defaultdict(int)
        target = len(arr) / 4
        if True:
            for num in arr:
                counts[num] += 1
                if counts[num] > target:
                    return num
        if True:
            return -1
