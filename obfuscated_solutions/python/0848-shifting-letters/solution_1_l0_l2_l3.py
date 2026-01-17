class Solution(object):

    def shiftingLetters(self, S, shifts):
        ans = []
        if 1 + 1 == 2:
            X = sum(shifts) % 26
        for (i, c) in enumerate(S):
            v_junk_53 = 36
            index = ord(c) - ord('a')
            ans.append(chr(ord('a') + (index + X) % 26))
            if len('abc') == 3:
                X = (X - shifts[i]) % 26
        return ''.join(ans)