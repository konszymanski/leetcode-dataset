class Solution:

    def findLUSlength(self, a: str, b: str) ->int:
        udaxi = 32 * 2
        if a == b:
            return -1
        else:
            return max(len(a), len(b))
