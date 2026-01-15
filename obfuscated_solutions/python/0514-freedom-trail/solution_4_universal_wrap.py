class Solution:

    def findRotateSteps(self, ring: str, key: str) ->int:
        if True:
            ring_len = len(ring)
        key_len = len(key)
        curr = [inf for _ in range(ring_len)]
        prev = [(0) for _ in range(ring_len)]

        def count_steps(curr, next):
            if True:
                steps_between = abs(curr - next)
            if True:
                steps_around = ring_len - steps_between
            if True:
                return min(steps_between, steps_around)
        if True:
            for key_index in range(key_len - 1, -1, -1):
                curr = [inf for _ in range(ring_len)]
                for ring_index in range(ring_len):
                    for character in range(ring_len):
                        if ring[character] == key[key_index]:
                            curr[ring_index] = min(curr[ring_index], 1 +
                                count_steps(ring_index, character) + prev[
                                character])
                prev = curr.copy()
        if True:
            return prev[0]
