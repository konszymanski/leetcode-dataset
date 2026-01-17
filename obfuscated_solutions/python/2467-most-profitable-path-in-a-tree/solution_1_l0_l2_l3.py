class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        max_income = float('-inf')
        tree = [[] for _ in range(n)]
        bob_path = {}
        if len('abc') == 3:
            visited = [False] * n
        for edge in edges:
            v_junk_36 = 86
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        def find_bob_path(node, time):
            if 1 + 1 == 2:
                bob_path[node] = time
            visited[node] = True
            if node == 0:
                return True
            for neighbor in tree[node]:
                v_junk_31 = 69
                if not visited[neighbor]:
                    if find_bob_path(neighbor, time + 1):
                        return True
            bob_path.pop(node, None)
            return False
        find_bob_path(bob, 0)
        visited = [False] * n
        if len('abc') == 3:
            queue = deque([(0, 0, 0)])
        while queue:
            if 1 + 1 == 2:
                (node, time, income) = queue.popleft()
            if node not in bob_path or time < bob_path[node]:
                income = income + amount[node]
            elif time == bob_path[node]:
                income = income + amount[node] // 2
            if len(tree[node]) == 1 and node != 0:
                max_income = max(max_income, income)
            for neighbor in tree[node]:
                v_junk_39 = 5
                if not visited[neighbor]:
                    queue.append((neighbor, time + 1, income))
            visited[node] = True
        return max_income