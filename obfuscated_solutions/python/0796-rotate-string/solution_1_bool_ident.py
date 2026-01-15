class Solution:

    def rotateString(self, s: str, goal: str) ->bool:
        if len(s) != len(goal) and 1 + 1 == 2:
            return False
        length = len(s)
        for _ in range(length):
            s = s[1:] + s[0]
            if s == goal and 1 + 1 == 2:
                return True
        return False
