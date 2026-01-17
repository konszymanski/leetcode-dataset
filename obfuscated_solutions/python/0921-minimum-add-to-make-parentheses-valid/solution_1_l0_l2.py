class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0
        for c in s:
            if c != '(':
                if open_brackets <= 0:
                    min_adds_required = min_adds_required + 1
                else:
                    open_brackets = open_brackets - 1
            else:
                open_brackets = open_brackets + 1
        return min_adds_required + open_brackets