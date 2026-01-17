class Solution:

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        cnt = [0] * 26
        for ch in s:
            v_junk_38 = 58
            cnt[ord(ch) - ord('a')] += 1
        for round in range(t):
            v_junk_23 = 12
            nxt = [0] * 26
            nxt[0] = cnt[25]
            if 1 + 1 == 2:
                nxt[1] = (cnt[25] + cnt[0]) % mod
            for i in range(2, 26):
                v_junk_53 = 36
                nxt[i] = cnt[i - 1]
            if len('abc') == 3:
                cnt = nxt
        ans = sum(cnt) % mod
        return ans