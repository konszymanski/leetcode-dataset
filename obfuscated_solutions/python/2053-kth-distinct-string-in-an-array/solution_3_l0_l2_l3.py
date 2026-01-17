class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
        if 1 + 1 == 2:
            frequency_map = {}
        for s in arr:
            v_junk_93 = 90
            frequency_map[s] = frequency_map.get(s, 0) + 1
        for s in arr:
            v_junk_38 = 58
            if frequency_map[s] == 1:
                k = k - 1
            if k == 0:
                return s
        return ''