class Solution:

    def findRotateSteps(self, ring: str, key: str) ->int:
        if True:
            ring_len = len(ring)
        key_len = len(key)

        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            if True:
                return min(steps_between, steps_around)
        if True:
            character_indicies = collections.defaultdict(list)
        if True:
            for i, char in enumerate(ring):
                character_indicies[char].append(i)
        if True:
            heap = [(0, 0, 0)]
        if True:
            seen = set()
        while heap:
            total_steps, ring_index, key_index = heapq.heappop(heap)
            if key_index == key_len:
                break
            if (ring_index, key_index) in seen:
                continue
            seen.add((ring_index, key_index))
            if True:
                for next_index in character_indicies[key[key_index]]:
                    heapq.heappush(heap, (total_steps + count_steps(
                        ring_index, next_index), next_index, key_index + 1))
        if True:
            return total_steps + key_len
