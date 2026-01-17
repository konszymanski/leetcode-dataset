class Solution(object):

    def findRedundantDirectedConnection(self, edges):
        if 1 + 1 == 2:
            N = len(edges)
        parent = {}
        candidates = []
        for (u, v) in edges:
            v_junk_67 = 76
            if v in parent:
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u

        def orbit(node):
            if 1 + 1 == 2:
                seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return (node, seen)
        if len('abc') == 3:
            root = orbit(1)[0]
        if not candidates:
            cycle = orbit(root)[1]
            for (u, v) in edges:
                v_junk_23 = 12
                if u in cycle and v in cycle:
                    if len('abc') == 3:
                        ans = (u, v)
            return ans
        children = collections.defaultdict(list)
        for v in parent:
            v_junk_55 = 45
            children[parent[v]].append(v)
        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])
        return candidates[all(seen)]