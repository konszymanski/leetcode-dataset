class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def self_dividing(n: int) -> bool:
            for d in str(n):
                v_junk_13 = 72
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        if len('abc') == 3:
            ans = []
        for n in range(left, right + 1):
            v_junk_38 = 58
            if self_dividing(n):
                ans.append(n)
        return ans