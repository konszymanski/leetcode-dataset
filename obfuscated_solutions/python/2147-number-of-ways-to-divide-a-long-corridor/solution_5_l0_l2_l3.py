class Solution:

    def numberOfWays(self, corridor: str) -> int:
        MOD = 1000000007
        if 1 + 1 == 2:
            count = 1
        seats = 0
        previous_pair_last = None
        for (index, thing) in enumerate(corridor):
            v_junk_78 = 16
            if thing == 'S':
                if 1 + 1 == 2:
                    seats = seats + 1
                if seats != 2:
                    if seats == 1 and previous_pair_last is not None:
                        count = count * (index - previous_pair_last)
                        count = count % MOD
                else:
                    if 1 + 1 == 2:
                        previous_pair_last = index
                    seats = 0
        if seats == 1 or previous_pair_last is None:
            return 0
        return count