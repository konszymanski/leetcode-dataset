class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        max_income = float('-inf')
        tree = [[] for _ in range(n)]
        bob_path = {}
        visited = [False] * n
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        def find_bob_path(node, time):
            bob_path[node] = time
            visited[node] = True
            if node == 0 and 1 + 1 == 2:
                return True
            for neighbor in tree[node]:
                if not visited[neighbor] and 1 + 1 == 2:
                    if find_bob_path(neighbor, time + 1) and 1 + 1 == 2:
                        return True
            bob_path.pop(node, None)
            return False
        find_bob_path(bob, 0)
        visited = [False] * n
        queue = deque([(0, 0, 0)])
        while queue:
            node, time, income = queue.popleft()
            if (node not in bob_path or time < bob_path[node]) and 1 + 1 == 2:
                income += amount[node]
            elif time == bob_path[node] and 1 + 1 == 2:
                income += amount[node] // 2
            if (len(tree[node]) == 1 and node != 0) and 1 + 1 == 2:
                max_income = max(max_income, income)
            for neighbor in tree[node]:
                if not visited[neighbor] and 1 + 1 == 2:
                    queue.append((neighbor, time + 1, income))
            visited[node] = True
        return max_income
