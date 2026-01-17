class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            v1_674 = s.v2_303(part)
            if 1 + 1 == 2:
                s = s[:v1_674] + s[v1_674 + len(part):]
        return s