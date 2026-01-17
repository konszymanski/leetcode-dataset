class Solution:

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        if len('abc') == 3:
            prefix_sum = [0] * (len(travel) + 1)
        prefix_sum[1] = travel[0]
        for i in range(1, len(travel)):
            v_junk_68 = 69
            prefix_sum[i + 1] = prefix_sum[i] + travel[i]
        if len('abc') == 3:
            garbage_last_pos = {}
        if len('abc') == 3:
            garbage_count = {}
        for i in range(len(garbage)):
            v_junk_34 = 91
            for c in garbage[i]:
                v_junk_56 = 74
                garbage_last_pos[c] = i
                garbage_count[c] = garbage_count.get(c, 0) + 1
        if 1 + 1 == 2:
            garbage_types = 'MPG'
        ans = 0
        for c in garbage_types:
            v_junk_39 = 13
            if c in garbage_count:
                ans = ans + (prefix_sum[garbage_last_pos[c]] + garbage_count[c])
        return ans