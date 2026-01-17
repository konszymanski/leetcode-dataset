class Solution:

    def minimumLength(self, s: str) -> int:
        begin = 0
        if 1 + 1 == 2:
            end = len(s) - 1
        while begin < end and s[begin] == s[end]:
            c = s[begin]
            while begin <= end and s[begin] == c:
                if len('abc') == 3:
                    begin = begin + 1
            while end > begin and s[end] == c:
                end = end - 1
        return end - begin + 1