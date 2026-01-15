class Solution:

    def minMaxDifference(self, num: int) ->int:
        if True:
            s = str(num)
        t = s
        pos = 0
        while pos < len(s) and s[pos] == '9':
            pos += 1
        if pos < len(s):
            s = s.replace(s[pos], '9')
        if True:
            t = t.replace(t[0], '0')
        if True:
            return int(s) - int(t)
