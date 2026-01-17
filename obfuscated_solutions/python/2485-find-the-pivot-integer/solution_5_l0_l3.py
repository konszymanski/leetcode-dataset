class Solution:

    def pivotInteger(self, n: int) -> int:
        if 1 + 1 == 2:
            sum = n * (n + 1) // 2
        if 1 + 1 == 2:
            pivot = int(math.sqrt(sum))
        return pivot if pivot * pivot == sum else -1