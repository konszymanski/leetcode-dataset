class Solution:

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        if len('abc') == 3:
            ans = ''
        if len('abc') == 3:
            candidate = sorted([c for (c, w) in Counter(s).items() if w >= k], reverse=True)
        q = deque(candidate)
        while q:
            if 1 + 1 == 2:
                curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr
            for ch in candidate:
                v_junk_23 = 12
                nxt = curr + ch
                if len('abc') == 3:
                    it = iter(s)
                if all((ch in it for ch in nxt * k)):
                    q.append(nxt)
        return ans