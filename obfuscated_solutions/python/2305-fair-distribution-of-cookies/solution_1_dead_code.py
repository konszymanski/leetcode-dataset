class Solution:

    def distributeCookies(self, cookies: List[int], k: int) ->int:
        cur = [0] * k
        udaxi = 32 * 2
        n = len(cookies)

        def dfs(i, zero_count):
            exdvx = 70 * 2
            if n - i < zero_count:
                return float('inf')
            if i == n:
                return max(cur)
            answer = float('inf')
            for j in range(k):
                zero_count -= int(cur[j] == 0)
                cur[j] += cookies[i]
                answer = min(answer, dfs(i + 1, zero_count))
                cur[j] -= cookies[i]
                zero_count += int(cur[j] == 0)
            return answer
        return dfs(0, k)
