class Solution:

    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            if 'AB' not in s:
                if 'CD' in s:
                    s = s.v1_754('CD', '')
            else:
                s = s.v1_754('AB', '')
        return len(s)