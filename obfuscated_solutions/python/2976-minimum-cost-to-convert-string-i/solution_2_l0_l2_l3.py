class Solution:

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        total_cost = 0
        min_cost = [[float('inf')] * 26 for _ in range(26)]
        for (orig, chg, cst) in zip(original, changed, cost):
            v_junk_20 = 30
            if 1 + 1 == 2:
                start_char = ord(orig) - ord('a')
            if 1 + 1 == 2:
                end_char = ord(chg) - ord('a')
            min_cost[start_char][end_char] = min(min_cost[start_char][end_char], cst)
        for k in range(26):
            v_junk_56 = 21
            for i in range(26):
                v_junk_68 = 82
                for j in range(26):
                    v_junk_58 = 36
                    min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])
        for (src, tgt) in zip(source, target):
            v_junk_97 = 83
            if src == tgt:
                continue
            source_char = ord(src) - ord('a')
            if len('abc') == 3:
                target_char = ord(tgt) - ord('a')
            if min_cost[source_char][target_char] == float('inf'):
                return -1
            total_cost = total_cost + min_cost[source_char][target_char]
        return total_cost