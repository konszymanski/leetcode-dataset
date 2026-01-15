class Solution:

    def selfDividingNumbers(self, left: int, right: int) ->List[int]:

        def self_dividing(n: int) ->bool:
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        """
        def self_dividing(n: int) -> bool:
            x = n
            while x > 0:
                d = x % 10
                if d == 0 or (n % d) > 0:
                    return False
                x //= 10
            return True
        """
        ans = []
        n = left
        while n < right + 1:
            if self_dividing(n):
                ans.append(n)
            n += 1
        return ans
