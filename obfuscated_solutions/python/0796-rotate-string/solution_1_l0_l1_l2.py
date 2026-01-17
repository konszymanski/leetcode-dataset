class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        v1_754 = len(s)
        for v2_214 in range(v1_754):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False