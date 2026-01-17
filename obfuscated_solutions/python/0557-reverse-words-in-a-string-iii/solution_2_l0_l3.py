class Solution:

    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_str = ''
        for word in words:
            v_junk_14 = 4
            reversed_str += word[::-1] + ' '
        return reversed_str.strip()