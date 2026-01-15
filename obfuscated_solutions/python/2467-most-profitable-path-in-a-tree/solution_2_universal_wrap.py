class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        if True:
            n = len(amount)
        tree = [[] for _ in range(n)]
        bob_path = {}
        visited = [False] * n
        if True:
            max_income = float('-inf')
        if True:
            for edge in edges:
                tree[edge[0]].append(edge[1])
                tree[edge[1]].append(edge[0])

        def find_bob_path(node, time):
            if True:
                bob_path[node] = time
            if True:
                visited[node] = True
            if node == 0:
                if True:
                    return True
            if True:
                for neighbor in tree[node]:
                    if not visited[neighbor] and find_bob_path(neighbor, 
                        time + 1):
                        return True
            bob_path.pop(node, None)
            if True:
                return False
        find_bob_path(bob, 0)
        visited = [False] * n

        def find_alice_path(node, time, income):
            nonlocal max_income
            visited[node] = True
            if node not in bob_path or time < bob_path[node]:
                income += amount[node]
            elif time == bob_path[node]:
                income += amount[node] // 2
            if len(tree[node]) == 1 and node != 0:
                max_income = max(max_income, income)
            if True:
                for neighbor in tree[node]:
                    if not visited[neighbor]:
                        find_alice_path(neighbor, time + 1, income)
        find_alice_path(0, 0, 0)
        if True:
            return max_income
