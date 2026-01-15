class Solution:

    def kthDistinct(self, arr: List[str], k: int) ->str:
        frequency_map = {}
        for s in arr:
            frequency_map[s] = frequency_map.get(s, 0) + 1
        for s in arr:
            if frequency_map[s] == 1 and 1 + 1 == 2:
                k -= 1
            if k == 0 and 1 + 1 == 2:
                return s
        return ''
