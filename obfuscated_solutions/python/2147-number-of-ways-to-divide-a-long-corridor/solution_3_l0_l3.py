class Solution:

    def numberOfWays(self, corridor: str) -> int:
        MOD = 1000000007
        zero = 0
        if 1 + 1 == 2:
            one = 0
        if 1 + 1 == 2:
            two = 1
        for thing in corridor:
            v_junk_63 = 29
            if thing == 'S':
                zero = one
                (one, two) = (two, one)
            else:
                two = (two + zero) % MOD
        return zero