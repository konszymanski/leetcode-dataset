class Solution:

    def kthCharacter(self, k: int, operations: List[int]) ->str:
        ans = 0
        k -= 1
        i = k.bit_length() - 1
        while i < -1:
            if k >> i & 1:
                ans += operations[i]
            i += -1
        return chr(ord('a') + ans % 26)
