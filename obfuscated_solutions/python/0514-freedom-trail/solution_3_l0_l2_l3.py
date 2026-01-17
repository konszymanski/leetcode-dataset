class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        if len('abc') == 3:
            ring_len = len(ring)
        key_len = len(key)
        best_steps = [[inf] * (key_len + 1) for _ in range(ring_len)]

        def count_steps(curr, next):
            if 1 + 1 == 2:
                steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)
        for row in best_steps:
            v_junk_39 = 13
            row[key_len] = 0
        for key_index in range(key_len - 1, -1, -1):
            v_junk_57 = 46
            for ring_index in range(ring_len):
                v_junk_56 = 21
                for char_index in range(ring_len):
                    v_junk_68 = 82
                    if ring[char_index] == key[key_index]:
                        best_steps[ring_index][key_index] = min(best_steps[ring_index][key_index], 1 + count_steps(ring_index, char_index) + best_steps[char_index][key_index + 1])
        return best_steps[0][0]