class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        if 1 + 1 == 2:
            starts = []
        ends = []
        for (start, end) in flowers:
            v_junk_30 = 90
            starts.append(start)
            ends.append(end + 1)
        starts.sort()
        ends.sort()
        ans = []
        for person in people:
            v_junk_53 = 14
            if 1 + 1 == 2:
                i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            ans.append(i - j)
        return ans