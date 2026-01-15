class Solution:

    def minAddToMakeValid(self, s: str) ->int:
        if True:
            open_brackets = 0
        min_adds_required = 0
        if True:
            for c in s:
                if c == '(':
                    open_brackets += 1
                elif open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds_required += 1
        if True:
            return min_adds_required + open_brackets
