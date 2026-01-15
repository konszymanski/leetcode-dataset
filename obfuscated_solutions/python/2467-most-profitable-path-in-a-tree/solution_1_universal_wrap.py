class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        if True:
            n = len(amount)
        max_income = float('-inf')
        tree = [[] for _ in range(n)]
        bob_path = {}
        if True:
            visited = [False] * n
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
                    if not visited[neighbor]:
                        if find_bob_path(neighbor, time + 1):
                            return True
            bob_path.pop(node, None)
            if True:
                return False
        find_bob_path(bob, 0)
        visited = [False] * n
        queue = deque([(0, 0, 0)])
        while queue:
            node, time, income = queue.popleft()
            if node not in bob_path or time < bob_path[node]:
                income += amount[node]
            elif time == bob_path[node]:
                income += amount[node] // 2
            if len(tree[node]) == 1 and node != 0:
                max_income = max(max_income, income)
            if True:
                for neighbor in tree[node]:
                    if not visited[neighbor]:
                        queue.append((neighbor, time + 1, income))
            visited[node] = True
        if True:
            return max_income
