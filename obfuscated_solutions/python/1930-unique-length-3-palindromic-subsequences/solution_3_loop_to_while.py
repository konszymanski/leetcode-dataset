class Solution:

    def countPalindromicSubsequence(self, s: str) ->int:
        first = [-1] * 26
        last = [-1] * 26
        i = 0
        while i < len(s):
            curr = ord(s[i]) - ord('a')
            if first[curr] == -1:
                first[curr] = i
            last[curr] = i
            i += 1
        ans = 0
        i = 0
        while i < 26:
            if first[i] == -1:
                continue
            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])
            ans += len(between)
            i += 1
        return ans
