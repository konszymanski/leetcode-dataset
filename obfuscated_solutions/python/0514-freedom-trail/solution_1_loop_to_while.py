class Solution:

    def findRotateSteps(self, ring: str, key: str) ->int:
        ring_len = len(ring)
        key_len = len(key)

        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        def try_lock(ring_index, key_index, min_steps):
            if key_index == len(key):
                return 0
            i = 0
            while i < len(ring):
                if ring[i] == key[key_index]:
                    total_steps = count_steps(ring_index, i) + 1 + try_lock(i,
                        key_index + 1, inf)
                    min_steps = min(min_steps, total_steps)
                i += 1
            return min_steps
        return try_lock(0, 0, inf)
