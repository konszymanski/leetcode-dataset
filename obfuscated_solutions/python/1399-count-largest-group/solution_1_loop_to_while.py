class Solution:

    def countLargestGroup(self, n: int) ->int:
        hashMap = collections.Counter()
        i = 1
        while i < n + 1:
            key = sum([int(x) for x in str(i)])
            hashMap[key] += 1
            i += 1
        maxValue = max(hashMap.values())
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count
