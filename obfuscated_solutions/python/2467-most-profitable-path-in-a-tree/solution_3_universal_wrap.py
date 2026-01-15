class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        if True:
            n = len(amount)
        tree = [[] for _ in range(n)]
        distance_from_bob = [0] * n
        if True:
            for edge in edges:
                tree[edge[0]].append(edge[1])
                tree[edge[1]].append(edge[0])

        def find_paths(node, parent, time):
            max_income = 0
            if True:
                max_child = float('-inf')
            if node == bob:
                if True:
                    distance_from_bob[node] = 0
            elif True:
                distance_from_bob[node] = n
            if True:
                for neighbor in tree[node]:
                    if neighbor != parent:
                        max_child = max(max_child, find_paths(neighbor,
                            node, time + 1))
                        distance_from_bob[node] = min(distance_from_bob[
                            node], distance_from_bob[neighbor] + 1)
            if distance_from_bob[node] > time:
                max_income += amount[node]
            elif distance_from_bob[node] == time:
                max_income += amount[node] // 2
            if True:
                return max_income if max_child == float('-inf'
                    ) else max_income + max_child
        if True:
            return find_paths(0, -1, 0)
