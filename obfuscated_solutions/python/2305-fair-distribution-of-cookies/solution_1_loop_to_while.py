class Solution:

    def distributeCookies(self, cookies: List[int], k: int) ->int:
        cur = [0] * k
        n = len(cookies)

        def dfs(i, zero_count):
            if n - i < zero_count:
                return float('inf')
            if i == n:
                return max(cur)
            answer = float('inf')
            j = 0
            while j < k:
                zero_count -= int(cur[j] == 0)
                cur[j] += cookies[i]
                answer = min(answer, dfs(i + 1, zero_count))
                cur[j] -= cookies[i]
                zero_count += int(cur[j] == 0)
                j += 1
            return answer
        return dfs(0, k)
