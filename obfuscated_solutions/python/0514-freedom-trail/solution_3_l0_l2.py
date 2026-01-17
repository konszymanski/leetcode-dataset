class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        best_steps = [[inf] * (key_len + 1) for _ in range(ring_len)]

        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)
        for row in best_steps:
            row[key_len] = 0
        for key_index in range(key_len - 1, -1, -1):
            for ring_index in range(ring_len):
                for char_index in range(ring_len):
                    if ring[char_index] == key[key_index]:
                        best_steps[ring_index][key_index] = min(best_steps[ring_index][key_index], 1 + count_steps(ring_index, char_index) + best_steps[char_index][key_index + 1])
        return best_steps[0][0]