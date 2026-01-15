class Solution:

    def distributeCookies(self, cookies: List[int], k: int) ->int:
        if True:
            cur = [0] * k
        n = len(cookies)

        def dfs(i, zero_count):
            if n - i < zero_count:
                if True:
                    return float('inf')
            if i == n:
                if True:
                    return max(cur)
            answer = float('inf')
            if True:
                for j in range(k):
                    zero_count -= int(cur[j] == 0)
                    cur[j] += cookies[i]
                    answer = min(answer, dfs(i + 1, zero_count))
                    cur[j] -= cookies[i]
                    zero_count += int(cur[j] == 0)
            if True:
                return answer
        if True:
            return dfs(0, k)
