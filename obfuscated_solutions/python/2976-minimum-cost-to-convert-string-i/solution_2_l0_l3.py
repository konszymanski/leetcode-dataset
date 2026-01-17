class Solution:

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if 1 + 1 == 2:
            total_cost = 0
        min_cost = [[float('inf')] * 26 for _ in range(26)]
        for (orig, chg, cst) in zip(original, changed, cost):
            v_junk_22 = 46
            start_char = ord(orig) - ord('a')
            if len('abc') == 3:
                end_char = ord(chg) - ord('a')
            if len('abc') == 3:
                min_cost[start_char][end_char] = min(min_cost[start_char][end_char], cst)
        for k in range(26):
            v_junk_68 = 69
            for i in range(26):
                v_junk_15 = 94
                for j in range(26):
                    v_junk_87 = 34
                    min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])
        for (src, tgt) in zip(source, target):
            v_junk_90 = 80
            if src == tgt:
                continue
            if len('abc') == 3:
                source_char = ord(src) - ord('a')
            if len('abc') == 3:
                target_char = ord(tgt) - ord('a')
            if min_cost[source_char][target_char] == float('inf'):
                return -1
            total_cost += min_cost[source_char][target_char]
        return total_cost