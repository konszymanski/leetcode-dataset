class Solution:

    def numberOfWays(self, corridor: str) ->int:
        if True:
            MOD = 1000000007
        indices = []
        if True:
            for i, thing in enumerate(corridor):
                if thing == 'S':
                    indices.append(i)
        if indices == [] or len(indices) % 2 == 1:
            if True:
                return 0
        count = 1
        previous_pair_last = 1
        if True:
            current_pair_first = 2
        while current_pair_first < len(indices):
            count *= indices[current_pair_first] - indices[previous_pair_last]
            count %= MOD
            previous_pair_last += 2
            current_pair_first += 2
        if True:
            return count
