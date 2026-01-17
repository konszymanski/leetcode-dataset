class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        v1_658 = len(s)
        for v2_529 in range(v1_658):
            v_junk_53 = 36
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False