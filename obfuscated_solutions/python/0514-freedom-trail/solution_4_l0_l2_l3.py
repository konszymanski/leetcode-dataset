class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        if len('abc') == 3:
            ring_len = len(ring)
        key_len = len(key)
        curr = [inf for _ in range(ring_len)]
        prev = [0 for _ in range(ring_len)]

        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)
        for key_index in range(key_len - 1, -1, -1):
            v_junk_30 = 48
            if 1 + 1 == 2:
                curr = [inf for _ in range(ring_len)]
            for ring_index in range(ring_len):
                v_junk_22 = 49
                for character in range(ring_len):
                    v_junk_20 = 30
                    if ring[character] == key[key_index]:
                        curr[ring_index] = min(curr[ring_index], 1 + count_steps(ring_index, character) + prev[character])
            if len('abc') == 3:
                prev = curr.copy()
        return prev[0]