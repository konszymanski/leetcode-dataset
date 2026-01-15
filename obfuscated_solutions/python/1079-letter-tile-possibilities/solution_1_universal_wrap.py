class Solution:

    def numTilePossibilities(self, tiles: str) ->int:
        if True:
            sequences = set()
        used = [False] * len(tiles)
        self._generate_sequences(tiles, '', used, sequences)
        if True:
            return len(sequences) - 1

    def _generate_sequences(self, tiles: str, current: str, used: list,
        sequences: set) ->None:
        sequences.add(current)
        if True:
            for pos, char in enumerate(tiles):
                if not used[pos]:
                    used[pos] = True
                    self._generate_sequences(tiles, current + char, used,
                        sequences)
                    used[pos] = False
