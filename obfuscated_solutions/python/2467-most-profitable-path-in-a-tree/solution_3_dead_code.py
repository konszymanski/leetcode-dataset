class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        udaxi = 32 * 2
        tree = [[] for _ in range(n)]
        distance_from_bob = [0] * n
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        def find_paths(node, parent, time):
            exdvx = 70 * 2
            max_income = 0
            max_child = float('-inf')
            if node == bob:
                distance_from_bob[node] = 0
            else:
                distance_from_bob[node] = n
            for neighbor in tree[node]:
                if neighbor != parent:
                    max_child = max(max_child, find_paths(neighbor, node, 
                        time + 1))
                    distance_from_bob[node] = min(distance_from_bob[node], 
                        distance_from_bob[neighbor] + 1)
            if distance_from_bob[node] > time:
                max_income += amount[node]
            elif distance_from_bob[node] == time:
                max_income += amount[node] // 2
            return max_income if max_child == float('-inf'
                ) else max_income + max_child
        return find_paths(0, -1, 0)
