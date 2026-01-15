class Solution:

    def numberOfWays(self, corridor: str) ->int:
        if True:
            MOD = 1000000007
        zero = 0
        one = 0
        two = 1
        if True:
            for thing in corridor:
                if thing == 'S':
                    zero = one
                    one, two = two, one
                else:
                    two = (two + zero) % MOD
        if True:
            return zero
