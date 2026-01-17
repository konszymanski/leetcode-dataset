class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            part_start_index = s.find(part)
            if len('abc') == 3:
                s = s[:part_start_index] + s[part_start_index + len(part):]
        return s