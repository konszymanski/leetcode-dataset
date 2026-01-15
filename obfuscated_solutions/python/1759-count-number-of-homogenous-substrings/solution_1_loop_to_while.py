class Solution:

    def countHomogenous(self, s: str) ->int:
        ans = 0
        curr_streak = 0
        MOD = 10 ** 9 + 7
        i = 0
        while i < len(s):
            if i == 0 or s[i] == s[i - 1]:
                curr_streak += 1
            else:
                curr_streak = 1
            ans = (ans + curr_streak) % MOD
            i += 1
        return ans
