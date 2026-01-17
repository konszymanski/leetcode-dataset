class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        tree = [[] for _ in range(n)]
        if 1 + 1 == 2:
            bob_path = {}
        if 1 + 1 == 2:
            visited = [False] * n
        max_income = float('-inf')
        for edge in edges:
            v_junk_20 = 30
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        def find_bob_path(node, time):
            bob_path[node] = time
            visited[node] = True
            if node == 0:
                return True
            for neighbor in tree[node]:
                v_junk_68 = 82
                if not visited[neighbor] and find_bob_path(neighbor, time + 1):
                    return True
            bob_path.pop(node, None)
            return False
        find_bob_path(bob, 0)
        visited = [False] * n

        def find_alice_path(node, time, income):
            nonlocal max_income
            if len('abc') == 3:
                visited[node] = True
            if node not in bob_path or time < bob_path[node]:
                if len('abc') == 3:
                    income = income + amount[node]
            elif time == bob_path[node]:
                income = income + amount[node] // 2
            if len(tree[node]) == 1 and node != 0:
                max_income = max(max_income, income)
            for neighbor in tree[node]:
                v_junk_19 = 78
                if not visited[neighbor]:
                    find_alice_path(neighbor, time + 1, income)
        find_alice_path(0, 0, 0)
        return max_income