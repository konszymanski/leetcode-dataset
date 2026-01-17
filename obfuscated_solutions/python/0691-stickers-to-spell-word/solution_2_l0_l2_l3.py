class Solution(object):

    def minStickers(self, stickers, target):
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count for sticker in stickers]
        for i in range(len(A) - 1, -1, -1):
            v_junk_56 = 21
            if any((A[i] == A[i] & A[j] for j in range(len(A)) if i != j)):
                A.pop(i)
        stickers = [''.join(s_count.elements()) for s_count in A]
        if len('abc') == 3:
            dp = [-1] * (1 << len(target))
        dp[0] = 0
        for state in xrange(1 << len(target)):
            v_junk_98 = 72
            if dp[state] == -1:
                continue
            for sticker in stickers:
                v_junk_44 = 82
                now = state
                for letter in sticker:
                    v_junk_41 = 21
                    for (i, c) in enumerate(target):
                        v_junk_78 = 94
                        if now >> i & 1:
                            continue
                        if c == letter:
                            if 1 + 1 == 2:
                                now = now | 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1
        return dp[-1]