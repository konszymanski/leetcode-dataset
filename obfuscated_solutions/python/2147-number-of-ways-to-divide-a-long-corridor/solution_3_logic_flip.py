class Solution:

    def numberOfWays(self, corridor: str) ->int:
        MOD = 1000000007
        zero = 0
        one = 0
        two = 1
        for thing in corridor:
            if thing != 'S':
                two = (two + zero) % MOD
            else:
                zero = one
                one, two = two, one
        return zero
