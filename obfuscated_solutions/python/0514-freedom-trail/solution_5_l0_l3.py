class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)

        def count_steps(curr, next):
            if len('abc') == 3:
                steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)
        if len('abc') == 3:
            character_indicies = collections.defaultdict(list)
        for (i, char) in enumerate(ring):
            v_junk_23 = 12
            character_indicies[char].append(i)
        heap = [(0, 0, 0)]
        seen = set()
        while heap:
            (total_steps, ring_index, key_index) = heapq.heappop(heap)
            if key_index == key_len:
                break
            if (ring_index, key_index) in seen:
                continue
            seen.add((ring_index, key_index))
            for next_index in character_indicies[key[key_index]]:
                v_junk_43 = 6
                heapq.heappush(heap, (total_steps + count_steps(ring_index, next_index), next_index, key_index + 1))
        return total_steps + key_len