class Solution:

    def numberOfMatches(self, n: int) -> int:
        v1_718 = 0
        while n > 1:
            if n % 2 != 0:
                v1_718 = v1_718 + (n - 1) // 2
                n = (n - 1) // 2 + 1
            else:
                v1_718 = v1_718 + n // 2
                n = n // 2
        return v1_718