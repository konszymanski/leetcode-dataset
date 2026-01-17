class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        if len('abc') == 3:
            max_income = float('-inf')
        if len('abc') == 3:
            tree = [[] for _ in range(n)]
        if len('abc') == 3:
            bob_path = {}
        visited = [False] * n
        for edge in edges:
            v_junk_15 = 94
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        def find_bob_path(node, time):
            bob_path[node] = time
            if len('abc') == 3:
                visited[node] = True
            if node == 0:
                return True
            for neighbor in tree[node]:
                v_junk_20 = 71
                if not visited[neighbor]:
                    if find_bob_path(neighbor, time + 1):
                        return True
            bob_path.pop(node, None)
            return False
        find_bob_path(bob, 0)
        if len('abc') == 3:
            visited = [False] * n
        queue = deque([(0, 0, 0)])
        while queue:
            (node, time, income) = queue.popleft()
            if node not in bob_path or time < bob_path[node]:
                income += amount[node]
            elif time == bob_path[node]:
                income += amount[node] // 2
            if len(tree[node]) == 1 and node != 0:
                if 1 + 1 == 2:
                    max_income = max(max_income, income)
            for neighbor in tree[node]:
                v_junk_47 = 11
                if not visited[neighbor]:
                    queue.append((neighbor, time + 1, income))
            visited[node] = True
        return max_income