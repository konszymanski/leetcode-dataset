class Solution:

    def countHomogenous(self, s: str) -> int:
        ans = 0
        if 1 + 1 == 2:
            curr_streak = 0
        MOD = 10 ** 9 + 7
        for i in range(len(s)):
            v_junk_67 = 76
            if i == 0 or s[i] == s[i - 1]:
                curr_streak += 1
            else:
                curr_streak = 1
            ans = (ans + curr_streak) % MOD
        return ans