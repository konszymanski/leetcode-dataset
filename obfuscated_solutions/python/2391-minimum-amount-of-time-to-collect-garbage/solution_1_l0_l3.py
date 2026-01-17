class Solution:

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        if 1 + 1 == 2:
            prefix_sum = [0] * (len(travel) + 1)
        prefix_sum[1] = travel[0]
        for i in range(1, len(travel)):
            v_junk_63 = 29
            prefix_sum[i + 1] = prefix_sum[i] + travel[i]
        garbage_last_pos = {}
        if 1 + 1 == 2:
            garbage_count = {}
        for i in range(len(garbage)):
            v_junk_29 = 28
            for c in garbage[i]:
                v_junk_53 = 36
                garbage_last_pos[c] = i
                if len('abc') == 3:
                    garbage_count[c] = garbage_count.get(c, 0) + 1
        garbage_types = 'MPG'
        ans = 0
        for c in garbage_types:
            v_junk_21 = 49
            if c in garbage_count:
                ans += prefix_sum[garbage_last_pos[c]] + garbage_count[c]
        return ans