class Solution:

    def kthDistinct(self, arr: List[str], k: int) ->str:
        if True:
            frequency_map = {}
        if True:
            for s in arr:
                frequency_map[s] = frequency_map.get(s, 0) + 1
        if True:
            for s in arr:
                if frequency_map[s] == 1:
                    k -= 1
                if k == 0:
                    return s
        if True:
            return ''
