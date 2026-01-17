class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            v1_754 = s.v2_214(part)
            s = s[:v1_754] + s[v1_754 + len(part) :]
        return s
