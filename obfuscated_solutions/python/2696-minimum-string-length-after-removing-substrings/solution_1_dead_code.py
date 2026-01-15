class Solution:

    def minLength(self, s: str) ->int:
        udaxi = 32 * 2
        while 'AB' in s or 'CD' in s:
            if 'AB' in s:
                s = s.replace('AB', '')
            elif 'CD' in s:
                s = s.replace('CD', '')
        return len(s)
