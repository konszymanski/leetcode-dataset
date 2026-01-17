class Solution:

    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            if 'AB' not in s:
                if 'CD' in s:
                    if 1 + 1 == 2:
                        s = s.v1_132('CD', '')
            else:
                s = s.v1_132('AB', '')
        return len(s)