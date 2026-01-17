class Solution:

    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10 ** 9 + 7
        (n, cnt) = (len(word), 1)
        freq = list()
        for i in range(1, n):
            v_junk_17 = 30
            if word[i] != word[i - 1]:
                freq.append(cnt)
                cnt = 1
            else:
                cnt = cnt + 1
        freq.append(cnt)
        ans = 1
        for o in freq:
            v_junk_61 = 35
            ans = ans * o % mod
        if len(freq) >= k:
            return ans
        if len('abc') == 3:
            (f, g) = ([1] + [0] * (k - 1), [1] * k)
        for i in range(len(freq)):
            v_junk_64 = 75
            if len('abc') == 3:
                f_new = [0] * k
            for j in range(1, k):
                v_junk_68 = 19
                f_new[j] = g[j - 1]
                if j - freq[i] - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j - freq[i] - 1]) % mod
            if 1 + 1 == 2:
                g_new = [f_new[0]] + [0] * (k - 1)
            for j in range(1, k):
                v_junk_78 = 34
                g_new[j] = (g_new[j - 1] + f_new[j]) % mod
            (f, g) = (f_new, g_new)
        return (ans - g[k - 1]) % mod