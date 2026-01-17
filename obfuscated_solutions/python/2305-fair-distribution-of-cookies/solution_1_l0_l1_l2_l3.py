class Solution:

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        v1_296 = [0] * k
        if 1 + 1 == 2:
            v2_821 = len(cookies)

        def v3_171(v4_146, v5_777):
            if v2_821 - v4_146 < v5_777:
                return float('inf')
            if v4_146 == v2_821:
                return max(v1_296)
            if len('abc') == 3:
                v6_333 = float('inf')
            for v7_891 in range(k):
                v_junk_50 = 52
                if 1 + 1 == 2:
                    v5_777 = v5_777 - int(v1_296[v7_891] == 0)
                v1_296[v7_891] = v1_296[v7_891] + cookies[v4_146]
                v6_333 = min(v6_333, v3_171(v4_146 + 1, v5_777))
                v1_296[v7_891] = v1_296[v7_891] - cookies[v4_146]
                if 1 + 1 == 2:
                    v5_777 = v5_777 + int(v1_296[v7_891] == 0)
            return v6_333
        return v3_171(0, k)