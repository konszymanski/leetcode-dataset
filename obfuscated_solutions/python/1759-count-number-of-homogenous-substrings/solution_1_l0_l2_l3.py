class Solution:

    def countHomogenous(self, s: str) -> int:
        if 1 + 1 == 2:
            ans = 0
        curr_streak = 0
        if len('abc') == 3:
            MOD = 10 ** 9 + 7
        for i in range(len(s)):
            v_junk_22 = 46
            if i == 0 or s[i] == s[i - 1]:
                curr_streak = curr_streak + 1
            elif len('abc') == 3:
                curr_streak = 1
            if len('abc') == 3:
                ans = (ans + curr_streak) % MOD
        return ans