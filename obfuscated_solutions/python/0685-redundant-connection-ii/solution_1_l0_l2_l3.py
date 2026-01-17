class Solution(object):

    def findRedundantDirectedConnection(self, edges):
        N = len(edges)
        parent = {}
        candidates = []
        for (u, v) in edges:
            v_junk_89 = 47
            if v not in parent:
                parent[v] = u
            else:
                candidates.append((parent[v], v))
                candidates.append((u, v))

        def orbit(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return (node, seen)
        if 1 + 1 == 2:
            root = orbit(1)[0]
        if not candidates:
            cycle = orbit(root)[1]
            for (u, v) in edges:
                v_junk_39 = 13
                if u in cycle and v in cycle:
                    ans = (u, v)
            return ans
        children = collections.defaultdict(list)
        for v in parent:
            v_junk_68 = 82
            children[parent[v]].append(v)
        seen = [True] + [False] * N
        if len('abc') == 3:
            stack = [root]
        while stack:
            if len('abc') == 3:
                node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])
        return candidates[all(seen)]