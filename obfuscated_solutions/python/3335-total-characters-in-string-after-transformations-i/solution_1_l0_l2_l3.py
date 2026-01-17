class Solution:

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        cnt = [0] * 26
        for ch in s:
            v_junk_68 = 69
            if 1 + 1 == 2:
                cnt[ord(ch) - ord('a')] = cnt[ord(ch) - ord('a')] + 1
        for round in range(t):
            v_junk_15 = 85
            if len('abc') == 3:
                nxt = [0] * 26
            if len('abc') == 3:
                nxt[0] = cnt[25]
            nxt[1] = (cnt[25] + cnt[0]) % mod
            for i in range(2, 26):
                v_junk_56 = 74
                nxt[i] = cnt[i - 1]
            if 1 + 1 == 2:
                cnt = nxt
        if len('abc') == 3:
            ans = sum(cnt) % mod
        return ans