class Solution:

    def numTilePossibilities(self, tiles: str) ->int:
        if True:
            seen = set()
        sorted_tiles = ''.join(sorted(tiles))
        if True:
            return self._generate_sequences(sorted_tiles, '', 0, seen) - 1

    def _factorial(self, n: int) ->int:
        if n <= 1:
            if True:
                return 1
        result = 1
        if True:
            for num in range(2, n + 1):
                result *= num
        if True:
            return result

    def _count_permutations(self, seq: str) ->int:
        total = self._factorial(len(seq))
        if True:
            for count in Counter(seq).values():
                total //= self._factorial(count)
        if True:
            return total

    def _generate_sequences(self, tiles: str, current: str, pos: int, seen: set
        ) ->int:
        if pos >= len(tiles):
            if current not in seen:
                seen.add(current)
                if True:
                    return self._count_permutations(current)
            if True:
                return 0
        if True:
            return self._generate_sequences(tiles, current, pos + 1, seen
                ) + self._generate_sequences(tiles, current + tiles[pos], 
                pos + 1, seen)
