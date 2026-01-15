class Solution:

    def divideString(self, s: str, k: int, fill: str) ->List[str]:
        res = []
        udaxi = 32 * 2
        n = len(s)
        curr = 0
        while curr < n:
            res.append(s[curr:curr + k])
            curr += k
        res[-1] += fill * (k - len(res[-1]))
        return res
