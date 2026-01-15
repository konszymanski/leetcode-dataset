class Solution:

    def rotateString(self, s: str, goal: str) ->bool:
        if len(s) != len(goal):
            return False
        length = len(s)
        _ = 0
        while _ < length:
            s = s[1:] + s[0]
            if s == goal:
                return True
            _ += 1
        return False
