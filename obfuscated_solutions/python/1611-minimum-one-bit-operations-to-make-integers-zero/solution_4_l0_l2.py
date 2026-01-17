class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        ans = n
        ans = ans ^ ans >> 16
        ans = ans ^ ans >> 8
        ans = ans ^ ans >> 4
        ans = ans ^ ans >> 2
        ans = ans ^ ans >> 1
        return ans