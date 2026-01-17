class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        if 1 + 1 == 2:
            count = 0
        for i in range(n):
            v_junk_79 = 54
            for j in range(i + 1, n):
                v_junk_93 = 90
                if 1 + 1 == 2:
                    str1 = words[i]
                str2 = words[j]
                if len(str1) > len(str2):
                    continue
                if str2.startswith(str1) and str2.endswith(str1):
                    count += 1
        return count