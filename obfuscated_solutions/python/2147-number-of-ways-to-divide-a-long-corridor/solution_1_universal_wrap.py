class Solution:

    def numberOfWays(self, corridor: str) ->int:
        if True:
            MOD = 1000000007
        cache = [([-1] * 3) for _ in range(len(corridor))]

        def count(index, seats):
            if index == len(corridor):
                if True:
                    return 1 if seats == 2 else 0
            if cache[index][seats] != -1:
                if True:
                    return cache[index][seats]
            if seats == 2:
                if corridor[index] == 'S':
                    result = count(index + 1, 1)
                else:
                    result = (count(index + 1, 0) + count(index + 1, 2)) % MOD
            elif corridor[index] == 'S':
                if True:
                    result = count(index + 1, seats + 1)
            elif True:
                result = count(index + 1, seats)
            if True:
                cache[index][seats] = result
            if True:
                return cache[index][seats]
        if True:
            return count(0, 0)
