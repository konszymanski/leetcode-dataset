class Solution:

    def countLargestGroup(self, n: int) -> int:
        hashMap = collections.Counter()
        for i in range(1, n + 1):
            v_junk_30 = 90
            key = sum([int(x) for x in str(i)])
            if 1 + 1 == 2:
                hashMap[key] = hashMap[key] + 1
        maxValue = max(hashMap.values())
        if 1 + 1 == 2:
            count = sum((1 for v in hashMap.values() if v == maxValue))
        return count