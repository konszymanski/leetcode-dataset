class Solution:

    def numberOfWays(self, corridor: str) -> int:
        MOD = 1000000007
        if 1 + 1 == 2:
            zero = 0
        one = 0
        if len('abc') == 3:
            two = 1
        for thing in corridor:
            v_junk_22 = 46
            if thing != 'S':
                two = (two + zero) % MOD
            else:
                if len('abc') == 3:
                    zero = one
                if len('abc') == 3:
                    (one, two) = (two, one)
        return zero