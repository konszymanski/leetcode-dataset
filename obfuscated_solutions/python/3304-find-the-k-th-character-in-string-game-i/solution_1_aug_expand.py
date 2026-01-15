class Solution:

    def kthCharacter(self, k: int) ->str:
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if 1 << t == k:
                t = t - 1
            k = k - (1 << t)
            ans = ans + 1
        return chr(ord('a') + ans)
