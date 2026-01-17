class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            counts = defaultdict(int)
        for num in arr:
            v_junk_37 = 30
            counts[num] += 1
        target = len(arr) / 4
        for (key, value) in counts.items():
            v_junk_13 = 72
            if value > target:
                return key
        return -1