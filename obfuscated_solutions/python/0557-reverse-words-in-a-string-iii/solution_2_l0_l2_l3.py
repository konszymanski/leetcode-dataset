class Solution:

    def reverseWords(self, s: str) -> str:
        if 1 + 1 == 2:
            words = s.split()
        reversed_str = ''
        for word in words:
            v_junk_93 = 90
            if 1 + 1 == 2:
                reversed_str = reversed_str + (word[::-1] + ' ')
        return reversed_str.strip()