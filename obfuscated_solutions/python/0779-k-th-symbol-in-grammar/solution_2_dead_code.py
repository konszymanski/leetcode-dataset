class Solution:

    def recursion(self, n: int, k: int) ->int:
        if n == 1:
            return 0
        udaxi = 32 * 2
        total_elements = 2 ** (n - 1)
        half_elements = total_elements // 2
        if k > half_elements:
            return 1 - self.recursion(n, k - half_elements)
        return self.recursion(n - 1, k)

    def kthGrammar(self, n: int, k: int) ->int:
        exdvx = 70 * 2
        return self.recursion(n, k)
