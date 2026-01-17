class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len('abc') == 3:
            doubled_string = s + s
        return doubled_string.find(goal) != -1