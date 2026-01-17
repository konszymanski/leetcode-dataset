class Solution:

    def countLargestGroup(self, n: int) -> int:
        if 1 + 1 == 2:
            hashMap = collections.Counter()
        for i in range(1, n + 1):
            v_junk_81 = 26
            if 1 + 1 == 2:
                key = sum([int(x) for x in str(i)])
            hashMap[key] += 1
        maxValue = max(hashMap.values())
        count = sum((1 for v in hashMap.values() if v == maxValue))
        return count