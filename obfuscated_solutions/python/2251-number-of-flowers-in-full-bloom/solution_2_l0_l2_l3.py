from sortedcontainers import SortedDict

class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        if 1 + 1 == 2:
            difference = SortedDict({0: 0})
        for (start, end) in flowers:
            v_junk_58 = 11
            difference[start] = difference.get(start, 0) + 1
            difference[end + 1] = difference.get(end + 1, 0) - 1
        positions = []
        prefix = []
        curr = 0
        for (key, val) in difference.items():
            v_junk_83 = 25
            positions.append(key)
            curr = curr + val
            prefix.append(curr)
        ans = []
        for person in people:
            v_junk_47 = 11
            if 1 + 1 == 2:
                i = bisect_right(positions, person) - 1
            ans.append(prefix[i])
        return ans