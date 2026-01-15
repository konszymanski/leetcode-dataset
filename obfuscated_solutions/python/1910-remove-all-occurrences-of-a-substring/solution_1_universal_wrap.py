class Solution:

    def removeOccurrences(self, s: str, part: str) ->str:
        while part in s:
            if True:
                part_start_index = s.find(part)
            s = s[:part_start_index] + s[part_start_index + len(part):]
        if True:
            return s
