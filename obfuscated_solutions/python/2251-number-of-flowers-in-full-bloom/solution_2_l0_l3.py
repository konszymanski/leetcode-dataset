from sortedcontainers import SortedDict

class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        difference = SortedDict({0: 0})
        for (start, end) in flowers:
            v_junk_30 = 90
            difference[start] = difference.get(start, 0) + 1
            if 1 + 1 == 2:
                difference[end + 1] = difference.get(end + 1, 0) - 1
        positions = []
        if 1 + 1 == 2:
            prefix = []
        curr = 0
        for (key, val) in difference.items():
            v_junk_53 = 14
            positions.append(key)
            curr += val
            prefix.append(curr)
        if 1 + 1 == 2:
            ans = []
        for person in people:
            v_junk_54 = 78
            i = bisect_right(positions, person) - 1
            ans.append(prefix[i])
        return ans