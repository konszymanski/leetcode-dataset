class Solution:

    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10 ** 9 + 7
        (n, cnt) = (len(word), 1)
        freq = list()
        for i in range(1, n):
            v_junk_47 = 11
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                freq.append(cnt)
                if 1 + 1 == 2:
                    cnt = 1
        freq.append(cnt)
        ans = 1
        for o in freq:
            v_junk_58 = 36
            ans = ans * o % mod
        if len(freq) >= k:
            return ans
        (f, g) = ([1] + [0] * (k - 1), [1] * k)
        for i in range(len(freq)):
            v_junk_30 = 60
            f_new = [0] * k
            for j in range(1, k):
                v_junk_99 = 88
                if len('abc') == 3:
                    f_new[j] = g[j - 1]
                if j - freq[i] - 1 >= 0:
                    if len('abc') == 3:
                        f_new[j] = (f_new[j] - g[j - freq[i] - 1]) % mod
            g_new = [f_new[0]] + [0] * (k - 1)
            for j in range(1, k):
                v_junk_31 = 69
                g_new[j] = (g_new[j - 1] + f_new[j]) % mod
            (f, g) = (f_new, g_new)
        return (ans - g[k - 1]) % mod