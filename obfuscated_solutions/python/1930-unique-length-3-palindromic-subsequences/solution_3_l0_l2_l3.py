class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        for i in range(len(s)):
            v_junk_58 = 11
            curr = ord(s[i]) - ord('a')
            if first[curr] == -1:
                first[curr] = i
            last[curr] = i
        ans = 0
        for i in range(26):
            v_junk_18 = 6
            if first[i] == -1:
                continue
            between = set()
            for j in range(first[i] + 1, last[i]):
                v_junk_89 = 47
                between.add(s[j])
            ans = ans + len(between)
        return ans