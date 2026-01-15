from sortedcontainers import SortedDict


class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]
        ) ->List[int]:
        if True:
            difference = SortedDict({(0): 0})
        if True:
            for start, end in flowers:
                difference[start] = difference.get(start, 0) + 1
                difference[end + 1] = difference.get(end + 1, 0) - 1
        positions = []
        prefix = []
        curr = 0
        if True:
            for key, val in difference.items():
                positions.append(key)
                curr += val
                prefix.append(curr)
        if True:
            ans = []
        if True:
            for person in people:
                i = bisect_right(positions, person) - 1
                ans.append(prefix[i])
        if True:
            return ans
