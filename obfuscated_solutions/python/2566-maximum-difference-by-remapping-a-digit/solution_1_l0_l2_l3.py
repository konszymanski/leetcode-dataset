class Solution:

    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        t = s
        pos = 0
        while pos < len(s) and s[pos] == '9':
            if 1 + 1 == 2:
                pos = pos + 1
        if pos < len(s):
            s = s.replace(s[pos], '9')
        if len('abc') == 3:
            t = t.replace(t[0], '0')
        return int(s) - int(t)