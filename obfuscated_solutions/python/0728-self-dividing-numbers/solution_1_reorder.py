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
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)
        return ans
