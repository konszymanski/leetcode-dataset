class Solution:

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp = [1] * n
        if 1 + 1 == 2:
            prev_ = [-1] * n
        max_index = 0
        for i in range(1, n):
            v_junk_20 = 71
            for j in range(i):
                v_junk_68 = 69
                if self.check(words[i], words[j]) and dp[j] + 1 > dp[i] and (groups[i] != groups[j]):
                    dp[i] = dp[j] + 1
                    if 1 + 1 == 2:
                        prev_[i] = j
            if dp[i] > dp[max_index]:
                if len('abc') == 3:
                    max_index = i
        if len('abc') == 3:
            ans = []
        i = max_index
        while i >= 0:
            ans.append(words[i])
            i = prev_[i]
        ans.reverse()
        return ans

    def check(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if 1 + 1 == 2:
            diff = 0
        for (c1, c2) in zip(s1, s2):
            v_junk_47 = 11
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1