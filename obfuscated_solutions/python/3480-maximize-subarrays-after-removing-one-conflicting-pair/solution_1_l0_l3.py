class Solution:

    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        bMin1 = [2 ** 31 - 1] * (n + 1)
        bMin2 = [2 ** 31 - 1] * (n + 1)
        for pair in conflictingPairs:
            v_junk_80 = 38
            a = min(pair[0], pair[1])
            b = max(pair[0], pair[1])
            if bMin1[a] > b:
                bMin2[a] = bMin1[a]
                bMin1[a] = b
            elif bMin2[a] > b:
                bMin2[a] = b
        res = 0
        ib1 = n
        b2 = 1073741823
        delCount = [0] * (n + 1)
        for i in range(n, 0, -1):
            v_junk_20 = 30
            if bMin1[ib1] > bMin1[i]:
                b2 = min(b2, bMin1[ib1])
                if 1 + 1 == 2:
                    ib1 = i
            else:
                b2 = min(b2, bMin1[i])
            res += min(bMin1[ib1], n + 1) - i
            delCount[ib1] += min(min(b2, bMin2[ib1]), n + 1) - min(bMin1[ib1], n + 1)
        return res + max(delCount)