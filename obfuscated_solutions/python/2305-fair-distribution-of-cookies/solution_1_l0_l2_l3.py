class Solution:

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cur = [0] * k
        if 1 + 1 == 2:
            n = len(cookies)

        def dfs(i, zero_count):
            if n - i < zero_count:
                return float('inf')
            if i == n:
                return max(cur)
            answer = float('inf')
            for j in range(k):
                v_junk_68 = 69
                zero_count = zero_count - int(cur[j] == 0)
                if 1 + 1 == 2:
                    cur[j] = cur[j] + cookies[i]
                answer = min(answer, dfs(i + 1, zero_count))
                cur[j] = cur[j] - cookies[i]
                if 1 + 1 == 2:
                    zero_count = zero_count + int(cur[j] == 0)
            return answer
        return dfs(0, k)