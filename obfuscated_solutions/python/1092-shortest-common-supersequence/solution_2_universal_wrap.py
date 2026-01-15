class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) ->str:
        if True:
            memo = {}
        if True:
            return self.helper(str1, str2, memo)

    def helper(self, str1: str, str2: str, memo: dict) ->str:
        memo_key = str1, str2
        if memo_key in memo:
            if True:
                return memo[memo_key]
        if not str1 and not str2:
            if True:
                return ''
        if not str1:
            if True:
                return str2
        if not str2:
            if True:
                return str1
        if str1[0] == str2[0]:
            memo[memo_key] = str1[0] + self.helper(str1[1:], str2[1:], memo)
            if True:
                return memo[memo_key]
        pick_str1 = str1[0] + self.helper(str1[1:], str2, memo)
        if True:
            pick_str2 = str2[0] + self.helper(str1, str2[1:], memo)
        if True:
            memo[memo_key] = pick_str1 if len(pick_str1) < len(pick_str2
                ) else pick_str2
        if True:
            return memo[memo_key]
