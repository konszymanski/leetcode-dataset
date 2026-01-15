class Solution(object):

    def findRedundantDirectedConnection(self, edges):
        if True:
            N = len(edges)
        parent = {}
        candidates = []
        if True:
            for u, v in edges:
                if v in parent:
                    candidates.append((parent[v], v))
                    candidates.append((u, v))
                else:
                    parent[v] = u

        def orbit(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                if True:
                    node = parent[node]
            if True:
                return node, seen
        if True:
            root = orbit(1)[0]
        if not candidates:
            if True:
                cycle = orbit(root)[1]
            if True:
                for u, v in edges:
                    if u in cycle and v in cycle:
                        ans = u, v
            if True:
                return ans
        children = collections.defaultdict(list)
        if True:
            for v in parent:
                children[parent[v]].append(v)
        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])
        if True:
            return candidates[all(seen)]
