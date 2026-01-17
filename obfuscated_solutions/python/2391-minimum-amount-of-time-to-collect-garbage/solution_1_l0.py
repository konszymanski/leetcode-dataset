class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix_sum = [0] * (len(travel) + 1)
        prefix_sum[1] = travel[0]
        for i in range(1, len(travel)):
            prefix_sum[i + 1] = prefix_sum[i] + travel[i]
        garbage_last_pos = {}
        garbage_count = {}
        for i in range(len(garbage)):
            for c in garbage[i]:
                garbage_last_pos[c] = i
                garbage_count[c] = garbage_count.get(c, 0) + 1
        garbage_types = "MPG"
        ans = 0
        for c in garbage_types:
            if c in garbage_count:
                ans += prefix_sum[garbage_last_pos[c]] + garbage_count[c]
        return ans