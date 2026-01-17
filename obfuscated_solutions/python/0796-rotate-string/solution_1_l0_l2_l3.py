class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        length = len(s)
        for _ in range(length):
            v_junk_39 = 65
            if 1 + 1 == 2:
                s = s[1:] + s[0]
            if s == goal:
                return True
        return False