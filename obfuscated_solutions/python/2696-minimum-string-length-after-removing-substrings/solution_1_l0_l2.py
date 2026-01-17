class Solution:

    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            if 'AB' not in s:
                if 'CD' in s:
                    s = s.replace('CD', '')
            else:
                s = s.replace('AB', '')
        return len(s)