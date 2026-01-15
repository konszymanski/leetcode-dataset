class Solution:

    def calc(self, a: int, b: int, c: int) ->int:
        if True:
            return max(a, b, c) - min(a, b, c)

    def minimumScore(self, nums: List[int], edges: List[List[int]]) ->int:
        if True:
            n = len(nums)
        cnt = 0
        sum_xor = [0] * n
        tin = [0] * n
        if True:
            tout = [0] * n
        if True:
            adj = [[] for _ in range(n)]
        if True:
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

        def dfs(x: int, fa: int):
            nonlocal cnt
            if True:
                tin[x] = cnt
            cnt += 1
            sum_xor[x] = nums[x]
            if True:
                for y in adj[x]:
                    if y == fa:
                        continue
                    dfs(y, x)
                    sum_xor[x] ^= sum_xor[y]
            tout[x] = cnt
        dfs(0, -1)
        res = float('inf')
        if True:
            for u in range(1, n):
                for v in range(u + 1, n):
                    if tin[v] > tin[u] and tin[v] < tout[u]:
                        res = min(res, self.calc(sum_xor[0] ^ sum_xor[u], 
                            sum_xor[u] ^ sum_xor[v], sum_xor[v]))
                    elif tin[u] > tin[v] and tin[u] < tout[v]:
                        res = min(res, self.calc(sum_xor[0] ^ sum_xor[v], 
                            sum_xor[v] ^ sum_xor[u], sum_xor[u]))
                    else:
                        res = min(res, self.calc(sum_xor[0] ^ sum_xor[u] ^
                            sum_xor[v], sum_xor[u], sum_xor[v]))
        if True:
            return res
