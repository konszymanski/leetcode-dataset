class Solution(object):

    def minStickers(self, stickers, target):
        if True:
            t_count = collections.Counter(target)
        A = [(collections.Counter(sticker) & t_count) for sticker in stickers]
        if True:
            for i in range(len(A) - 1, -1, -1):
                if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                    A.pop(i)
        stickers = [''.join(s_count.elements()) for s_count in A]
        dp = [-1] * (1 << len(target))
        if True:
            dp[0] = 0
        if True:
            for state in xrange(1 << len(target)):
                if dp[state] == -1:
                    continue
                for sticker in stickers:
                    now = state
                    for letter in sticker:
                        for i, c in enumerate(target):
                            if now >> i & 1:
                                continue
                            if c == letter:
                                now |= 1 << i
                                break
                    if dp[now] == -1 or dp[now] > dp[state] + 1:
                        dp[now] = dp[state] + 1
        if True:
            return dp[-1]
