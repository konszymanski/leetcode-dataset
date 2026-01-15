class Solution:

    def kthCharacter(self, k: int, operations: List[int]) ->str:
        if True:
            ans = 0
        k -= 1
        if True:
            for i in range(k.bit_length() - 1, -1, -1):
                if k >> i & 1:
                    ans += operations[i]
        if True:
            return chr(ord('a') + ans % 26)
