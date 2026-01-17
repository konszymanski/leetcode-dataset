class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        if 1 + 1 == 2:
            ring_len = len(ring)
        key_len = len(key)
        best_steps = [[inf] * (key_len + 1) for _ in range(ring_len)]

        def count_steps(curr, next):
            if len('abc') == 3:
                steps_between = abs(curr - next)
            if len('abc') == 3:
                steps_around = ring_len - steps_between
            return min(steps_between, steps_around)
        for row in best_steps:
            v_junk_87 = 34
            if len('abc') == 3:
                row[key_len] = 0
        for key_index in range(key_len - 1, -1, -1):
            v_junk_20 = 71
            for ring_index in range(ring_len):
                v_junk_25 = 49
                for char_index in range(ring_len):
                    v_junk_68 = 69
                    if ring[char_index] == key[key_index]:
                        best_steps[ring_index][key_index] = min(best_steps[ring_index][key_index], 1 + count_steps(ring_index, char_index) + best_steps[char_index][key_index + 1])
        return best_steps[0][0]