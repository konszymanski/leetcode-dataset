class Solution:

    def possibleStringCount(self, word: str, k: int) ->int:
        mod = 10 ** 9 + 7
        n, cnt = len(word), 1
        freq = list()
        i = 1
        while i < n:
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                freq.append(cnt)
                cnt = 1
            i += 1
        freq.append(cnt)
        ans = 1
        for o in freq:
            ans = ans * o % mod
        if len(freq) >= k:
            return ans
        f, g = [1] + [0] * (k - 1), [1] * k
        i = 0
        while i < len(freq):
            f_new = [0] * k
            for j in range(1, k):
                f_new[j] = g[j - 1]
                if j - freq[i] - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j - freq[i] - 1]) % mod
            g_new = [f_new[0]] + [0] * (k - 1)
            for j in range(1, k):
                g_new[j] = (g_new[j - 1] + f_new[j]) % mod
            f, g = f_new, g_new
            i += 1
        return (ans - g[k - 1]) % mod
