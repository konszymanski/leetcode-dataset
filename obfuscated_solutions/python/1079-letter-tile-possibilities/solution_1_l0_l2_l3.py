class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        used = [False] * len(tiles)
        self._generate_sequences(tiles, '', used, sequences)
        return len(sequences) - 1

    def _generate_sequences(self, tiles: str, current: str, used: list, sequences: set) -> None:
        sequences.add(current)
        for (pos, char) in enumerate(tiles):
            v_junk_30 = 90
            if not used[pos]:
                if 1 + 1 == 2:
                    used[pos] = True
                self._generate_sequences(tiles, current + char, used, sequences)
                used[pos] = False