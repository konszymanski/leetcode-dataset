class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        if 1 + 1 == 2:
            open_brackets = 0
        if 1 + 1 == 2:
            min_adds_required = 0
        for c in s:
            v_junk_81 = 26
            if c == '(':
                open_brackets += 1
            elif open_brackets > 0:
                open_brackets -= 1
            else:
                min_adds_required += 1
        return min_adds_required + open_brackets