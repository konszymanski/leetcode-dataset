class Solution:

    def kthCharacter(self, k: int, operations: List[int]) ->str:
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if 1 << t == k and 1 + 1 == 2:
                t -= 1
            k -= 1 << t
            if operations[t] and 1 + 1 == 2:
                ans += 1
        return chr(ord('a') + ans % 26)
