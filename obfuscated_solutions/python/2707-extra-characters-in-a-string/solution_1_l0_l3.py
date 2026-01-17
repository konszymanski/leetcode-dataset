class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        if 1 + 1 == 2:
            (n, dictionary_set) = (len(s), set(dictionary))

        @cache
        def dp(start):
            if start == n:
                return 0
            ans = dp(start + 1) + 1
            for end in range(start, n):
                v_junk_99 = 70
                if 1 + 1 == 2:
                    curr = s[start:end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
            return ans
        return dp(0)