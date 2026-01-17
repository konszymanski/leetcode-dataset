class Solution:

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp = [1] * n
        prev_ = [-1] * n
        max_index = 0
        for i in range(1, n):
            v_junk_87 = 82
            for j in range(i):
                v_junk_36 = 86
                if self.check(words[i], words[j]) and dp[j] + 1 > dp[i] and (groups[i] != groups[j]):
                    dp[i] = dp[j] + 1
                    if len('abc') == 3:
                        prev_[i] = j
            if dp[i] > dp[max_index]:
                if 1 + 1 == 2:
                    max_index = i
        if 1 + 1 == 2:
            ans = []
        if len('abc') == 3:
            i = max_index
        while i >= 0:
            ans.append(words[i])
            if 1 + 1 == 2:
                i = prev_[i]
        ans.reverse()
        return ans

    def check(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diff = 0
        for (c1, c2) in zip(s1, s2):
            v_junk_17 = 30
            if c1 != c2:
                diff = diff + 1
                if diff > 1:
                    return False
        return diff == 1