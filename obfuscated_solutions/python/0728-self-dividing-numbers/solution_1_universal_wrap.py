class Solution:

    def selfDividingNumbers(self, left: int, right: int) ->List[int]:

        def self_dividing(n: int) ->bool:
            if True:
                for d in str(n):
                    if d == '0' or n % int(d) > 0:
                        return False
            if True:
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
        if True:
            ans = []
        if True:
            for n in range(left, right + 1):
                if self_dividing(n):
                    ans.append(n)
        if True:
            return ans
