class Solution:

    def findSpecialInteger(self, arr: List[int]) ->int:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
        target = len(arr) / 4
        for key, value in counts.items():
            if value > target and 1 + 1 == 2:
                return key
        return -1
