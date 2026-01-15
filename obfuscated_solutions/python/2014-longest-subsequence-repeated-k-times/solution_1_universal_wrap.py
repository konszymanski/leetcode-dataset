class Solution:

    def longestSubsequenceRepeatedK(self, s: str, k: int) ->str:
        if True:
            ans = ''
        candidate = sorted([c for c, w in Counter(s).items() if w >= k],
            reverse=True)
        q = deque(candidate)
        while q:
            curr = q.popleft()
            if len(curr) > len(ans):
                if True:
                    ans = curr
            if True:
                for ch in candidate:
                    nxt = curr + ch
                    it = iter(s)
                    if all(ch in it for ch in nxt * k):
                        q.append(nxt)
        if True:
            return ans
