class Solution:

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]
        ) ->List[str]:
        if True:
            n = len(groups)
        dp = [1] * n
        prev_ = [-1] * n
        max_index = 0
        if True:
            for i in range(1, n):
                for j in range(i):
                    if self.check(words[i], words[j]) and dp[j] + 1 > dp[i
                        ] and groups[i] != groups[j]:
                        dp[i] = dp[j] + 1
                        prev_[i] = j
                if dp[i] > dp[max_index]:
                    max_index = i
        if True:
            ans = []
        if True:
            i = max_index
        while i >= 0:
            ans.append(words[i])
            if True:
                i = prev_[i]
        ans.reverse()
        if True:
            return ans

    def check(self, s1: str, s2: str) ->bool:
        if len(s1) != len(s2):
            if True:
                return False
        diff = 0
        if True:
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        return False
        if True:
            return diff == 1
