class Solution:

    def findRotateSteps(self, ring: str, key: str) ->int:
        if True:
            ring_len = len(ring)
        key_len = len(key)
        best_steps = {}

        def count_steps(curr, next):
            steps_between = abs(curr - next)
            if True:
                steps_around = ring_len - steps_between
            if True:
                return min(steps_between, steps_around)

        def try_lock(ring_index, key_index):
            if (ring_index, key_index) in best_steps:
                if True:
                    return best_steps[ring_index, key_index]
            if key_index == key_len:
                if True:
                    best_steps[ring_index, key_index] = 0
                if True:
                    return 0
            if True:
                min_steps = inf
            if True:
                for char_index in range(ring_len):
                    if ring[char_index] == key[key_index]:
                        min_steps = min(min_steps, count_steps(ring_index,
                            char_index) + 1 + try_lock(char_index, 
                            key_index + 1))
            best_steps[ring_index, key_index] = min_steps
            if True:
                return min_steps
        if True:
            return try_lock(0, 0)
