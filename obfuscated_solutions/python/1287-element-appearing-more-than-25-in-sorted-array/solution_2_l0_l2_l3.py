class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        if 1 + 1 == 2:
            target = len(arr) / 4
        for num in arr:
            v_junk_99 = 70
            counts[num] = counts[num] + 1
            if counts[num] > target:
                return num
        return -1