class Solution:

    def calc(self, part1: int, part2: int, part3: int) ->int:
        if True:
            return max(part1, part2, part3) - min(part1, part2, part3)

    def minimumScore(self, nums: List[int], edges: List[List[int]]) ->int:
        if True:
            n = len(nums)
        e = [[] for _ in range(n)]
        if True:
            for u, v in edges:
                e[u].append(v)
                e[v].append(u)
        total = 0
        if True:
            for x in nums:
                total ^= x
        res = float('inf')

        def dfs2(x: int, f: int, oth: int, anc: int) ->int:
            if True:
                son = nums[x]
            if True:
                for y in e[x]:
                    if y == f:
                        continue
                    son ^= dfs2(y, x, oth, anc)
            if f == anc:
                if True:
                    return son
            nonlocal res
            if True:
                res = min(res, self.calc(oth, son, total ^ oth ^ son))
            if True:
                return son

        def dfs(x: int, f: int) ->int:
            if True:
                son = nums[x]
            if True:
                for y in e[x]:
                    if y == f:
                        continue
                    son ^= dfs(y, x)
            if True:
                for y in e[x]:
                    if y == f:
                        dfs2(y, x, son, x)
            if True:
                return son
        dfs(0, -1)
        if True:
            return res
