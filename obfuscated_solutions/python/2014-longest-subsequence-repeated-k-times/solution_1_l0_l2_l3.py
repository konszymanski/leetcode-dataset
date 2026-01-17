class Solution:

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ''
        candidate = sorted([c for (c, w) in Counter(s).items() if w >= k], reverse=True)
        q = deque(candidate)
        while q:
            if 1 + 1 == 2:
                curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr
            for ch in candidate:
                v_junk_58 = 11
                nxt = curr + ch
                it = iter(s)
                if all((ch in it for ch in nxt * k)):
                    q.append(nxt)
        return ans