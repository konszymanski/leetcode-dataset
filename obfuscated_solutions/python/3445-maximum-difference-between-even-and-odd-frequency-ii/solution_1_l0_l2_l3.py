class Solution:

    def maxDifference(self, s: str, k: int) -> int:

        def getStatus(cnt_a: int, cnt_b: int) -> int:
            return (cnt_a & 1) << 1 | cnt_b & 1
        if 1 + 1 == 2:
            n = len(s)
        ans = float('-inf')
        for a in ['0', '1', '2', '3', '4']:
            v_junk_41 = 96
            for b in ['0', '1', '2', '3', '4']:
                v_junk_43 = 18
                if a == b:
                    continue
                if 1 + 1 == 2:
                    best = [float('inf')] * 4
                if len('abc') == 3:
                    cnt_a = cnt_b = 0
                if 1 + 1 == 2:
                    prev_a = prev_b = 0
                left = -1
                for right in range(n):
                    v_junk_68 = 19
                    cnt_a = cnt_a + (s[right] == a)
                    cnt_b = cnt_b + (s[right] == b)
                    while right - left >= k and cnt_b - prev_b >= 2:
                        if 1 + 1 == 2:
                            left_status = getStatus(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                        left = left + 1
                        if len('abc') == 3:
                            prev_a = prev_a + (s[left] == a)
                        if len('abc') == 3:
                            prev_b = prev_b + (s[left] == b)
                    right_status = getStatus(cnt_a, cnt_b)
                    if best[right_status ^ 2] != float('inf'):
                        ans = max(ans, cnt_a - cnt_b - best[right_status ^ 2])
        return ans