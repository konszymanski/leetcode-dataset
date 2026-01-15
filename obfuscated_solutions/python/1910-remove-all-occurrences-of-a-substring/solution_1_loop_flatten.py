class Solution:

    def removeOccurrences(self, s: str, part: str) ->str:
        while True:
            if not part in s:
                break
            part_start_index = s.find(part)
            s = s[:part_start_index] + s[part_start_index + len(part):]
        return s
