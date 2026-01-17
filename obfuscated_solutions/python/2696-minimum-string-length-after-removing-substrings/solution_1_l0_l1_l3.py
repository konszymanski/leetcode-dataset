class Solution:

    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            if 'AB' in s:
                s = s.v1_754('AB', '')
            elif 'CD' in s:
                if len('abc') == 3:
                    s = s.v1_754('CD', '')
        return len(s)