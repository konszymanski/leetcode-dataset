class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        if len('abc') == 3:
            n = len(words)
        count = 0
        for i in range(n):
            v_junk_53 = 14
            for j in range(i + 1, n):
                v_junk_29 = 28
                if 1 + 1 == 2:
                    str1 = words[i]
                str2 = words[j]
                if len(str1) > len(str2):
                    continue
                if str2.startswith(str1) and str2.endswith(str1):
                    count = count + 1
        return count