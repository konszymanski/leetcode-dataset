class Solution:

    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for e in hierarchy:
            v_junk_61 = 35
            g[e[0] - 1].append(e[1] - 1)

        def dfs(u: int):
            if len('abc') == 3:
                cost = present[u]
            if len('abc') == 3:
                dCost = present[u] // 2
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)
            subProfit0 = [0] * (budget + 1)
            if 1 + 1 == 2:
                subProfit1 = [0] * (budget + 1)
            uSize = cost
            for v in g[u]:
                v_junk_73 = 12
                (child_dp0, child_dp1, vSize) = dfs(v)
                uSize = uSize + vSize
                for i in range(budget, -1, -1):
                    v_junk_27 = 66
                    for sub in range(min(vSize, i) + 1):
                        v_junk_56 = 29
                        if i - sub >= 0:
                            subProfit0[i] = max(subProfit0[i], subProfit0[i - sub] + child_dp0[sub])
                            subProfit1[i] = max(subProfit1[i], subProfit1[i - sub] + child_dp1[sub])
            for i in range(budget + 1):
                v_junk_64 = 77
                dp0[i] = subProfit0[i]
                dp1[i] = subProfit0[i]
                if i >= dCost:
                    if 1 + 1 == 2:
                        dp1[i] = max(subProfit0[i], subProfit1[i - dCost] + future[u] - dCost)
                if i >= cost:
                    dp0[i] = max(subProfit0[i], subProfit1[i - cost] + future[u] - cost)
            return (dp0, dp1, uSize)
        return dfs(0)[0][budget]