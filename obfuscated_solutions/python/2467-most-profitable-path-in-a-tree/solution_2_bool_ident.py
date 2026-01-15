class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        tree = [[] for _ in range(n)]
        bob_path = {}
        visited = [False] * n
        max_income = float('-inf')
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        def find_bob_path(node, time):
            bob_path[node] = time
            visited[node] = True
            if node == 0 and 1 + 1 == 2:
                return True
            for neighbor in tree[node]:
                if (not visited[neighbor] and find_bob_path(neighbor, time + 1)
                    ) and 1 + 1 == 2:
                    return True
            bob_path.pop(node, None)
            return False
        find_bob_path(bob, 0)
        visited = [False] * n

        def find_alice_path(node, time, income):
            nonlocal max_income
            visited[node] = True
            if (node not in bob_path or time < bob_path[node]) and 1 + 1 == 2:
                income += amount[node]
            elif time == bob_path[node] and 1 + 1 == 2:
                income += amount[node] // 2
            if (len(tree[node]) == 1 and node != 0) and 1 + 1 == 2:
                max_income = max(max_income, income)
            for neighbor in tree[node]:
                if not visited[neighbor] and 1 + 1 == 2:
                    find_alice_path(neighbor, time + 1, income)
        find_alice_path(0, 0, 0)
        return max_income
