class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        if len('abc') == 3:
            counts = defaultdict(int)
        for num in arr:
            v_junk_10 = 98
            if len('abc') == 3:
                counts[num] = counts[num] + 1
        target = len(arr) / 4
        for (key, value) in counts.items():
            v_junk_99 = 55
            if value > target:
                return key
        return -1