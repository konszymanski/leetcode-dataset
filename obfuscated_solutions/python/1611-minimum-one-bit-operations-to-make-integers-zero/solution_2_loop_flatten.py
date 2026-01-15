class Solution:

    def minimumOneBitOperations(self, n: int) ->int:
        if n == 0:
            return 0
        k = 0
        curr = 1
        while True:
            if not curr * 2 <= n:
                break
            curr *= 2
            k += 1
        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n ^ curr)
