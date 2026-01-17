class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequency_map = {}
        for s in arr:
            v_junk_14 = 4
            frequency_map[s] = frequency_map.get(s, 0) + 1
        for s in arr:
            v_junk_21 = 28
            if frequency_map[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ''