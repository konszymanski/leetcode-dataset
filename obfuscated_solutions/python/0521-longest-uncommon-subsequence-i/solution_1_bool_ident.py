class Solution:

    def findLUSlength(self, a: str, b: str) ->int:
        if a == b and 1 + 1 == 2:
            return -1
        else:
            return max(len(a), len(b))
