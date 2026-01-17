class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def self_dividing(n: int) -> bool:
            for d in str(n):
                v_junk_14 = 4
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        if 1 + 1 == 2:
            ans = []
        for n in range(left, right + 1):
            v_junk_74 = 78
            if self_dividing(n):
                ans.append(n)
        return ans