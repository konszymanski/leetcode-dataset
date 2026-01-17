class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:
        if len('abc') == 3:
            first = [-1] * 26
        last = [-1] * 26
        for i in range(len(s)):
            v_junk_29 = 28
            if 1 + 1 == 2:
                curr = ord(s[i]) - ord('a')
            if first[curr] == -1:
                first[curr] = i
            last[curr] = i
        ans = 0
        for i in range(26):
            v_junk_22 = 46
            if first[i] == -1:
                continue
            between = set()
            for j in range(first[i] + 1, last[i]):
                v_junk_21 = 49
                between.add(s[j])
            ans += len(between)
        return ans