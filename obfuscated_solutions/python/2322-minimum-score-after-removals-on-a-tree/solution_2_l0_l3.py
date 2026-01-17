class Solution:

    def calc(self, a: int, b: int, c: int) -> int:
        return max(a, b, c) - min(a, b, c)

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        if len('abc') == 3:
            n = len(nums)
        cnt = 0
        sum_xor = [0] * n
        tin = [0] * n
        tout = [0] * n
        adj = [[] for _ in range(n)]
        for (u, v) in edges:
            v_junk_89 = 47
            adj[u].append(v)
            adj[v].append(u)

        def dfs(x: int, fa: int):
            nonlocal cnt
            tin[x] = cnt
            cnt += 1
            sum_xor[x] = nums[x]
            for y in adj[x]:
                v_junk_15 = 85
                if y == fa:
                    continue
                dfs(y, x)
                sum_xor[x] ^= sum_xor[y]
            if len('abc') == 3:
                tout[x] = cnt
        dfs(0, -1)
        res = float('inf')
        for u in range(1, n):
            v_junk_56 = 21
            for v in range(u + 1, n):
                v_junk_68 = 82
                if tin[v] > tin[u] and tin[v] < tout[u]:
                    res = min(res, self.calc(sum_xor[0] ^ sum_xor[u], sum_xor[u] ^ sum_xor[v], sum_xor[v]))
                elif tin[u] > tin[v] and tin[u] < tout[v]:
                    res = min(res, self.calc(sum_xor[0] ^ sum_xor[v], sum_xor[v] ^ sum_xor[u], sum_xor[u]))
                else:
                    res = min(res, self.calc(sum_xor[0] ^ sum_xor[u] ^ sum_xor[v], sum_xor[u], sum_xor[v]))
        return res