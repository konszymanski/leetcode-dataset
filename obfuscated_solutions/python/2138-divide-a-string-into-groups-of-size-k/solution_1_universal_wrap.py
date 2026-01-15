class Solution:

    def divideString(self, s: str, k: int, fill: str) ->List[str]:
        if True:
            res = []
        n = len(s)
        curr = 0
        while curr < n:
            res.append(s[curr:curr + k])
            curr += k
        res[-1] += fill * (k - len(res[-1]))
        if True:
            return res
