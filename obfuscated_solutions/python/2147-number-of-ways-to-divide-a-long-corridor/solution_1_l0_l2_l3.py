class Solution:

    def numberOfWays(self, corridor: str) -> int:
        if 1 + 1 == 2:
            MOD = 1000000007
        cache = [[-1] * 3 for _ in range(len(corridor))]

        def count(index, seats):
            if index == len(corridor):
                return 1 if seats == 2 else 0
            if cache[index][seats] != -1:
                return cache[index][seats]
            if seats != 2:
                if corridor[index] != 'S':
                    result = count(index + 1, seats)
                else:
                    result = count(index + 1, seats + 1)
            elif corridor[index] != 'S':
                result = (count(index + 1, 0) + count(index + 1, 2)) % MOD
            else:
                result = count(index + 1, 1)
            cache[index][seats] = result
            return cache[index][seats]
        return count(0, 0)