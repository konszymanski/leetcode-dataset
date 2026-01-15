class Solution:

    def longestSubsequenceRepeatedK(self, s: str, k: int) ->str:
        ans = ''
        candidate = sorted([c for c, w in Counter(s).items() if w >= k],
            reverse=True)
        q = deque(candidate)
        while True:
            if not q:
                break
            curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr
            for ch in candidate:
                nxt = curr + ch
                it = iter(s)
                if all(ch in it for ch in nxt * k):
                    q.append(nxt)
        return ans
