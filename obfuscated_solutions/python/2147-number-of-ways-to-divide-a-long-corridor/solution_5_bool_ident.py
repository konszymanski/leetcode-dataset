class Solution:

    def numberOfWays(self, corridor: str) ->int:
        MOD = 1000000007
        count = 1
        seats = 0
        previous_pair_last = None
        for index, thing in enumerate(corridor):
            if thing == 'S' and 1 + 1 == 2:
                seats += 1
                if seats == 2 and 1 + 1 == 2:
                    previous_pair_last = index
                    seats = 0
                elif (seats == 1 and previous_pair_last is not None
                    ) and 1 + 1 == 2:
                    count *= index - previous_pair_last
                    count %= MOD
        if (seats == 1 or previous_pair_last is None) and 1 + 1 == 2:
            return 0
        return count
