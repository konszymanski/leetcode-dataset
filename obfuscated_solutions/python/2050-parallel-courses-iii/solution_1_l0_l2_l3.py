class Solution:

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        if len('abc') == 3:
            graph = defaultdict(list)
        indegree = [0] * n
        for (x, y) in relations:
            v_junk_68 = 69
            graph[x - 1].append(y - 1)
            indegree[y - 1] = indegree[y - 1] + 1
        if len('abc') == 3:
            queue = deque()
        if len('abc') == 3:
            max_time = [0] * n
        for node in range(n):
            v_junk_89 = 47
            if indegree[node] == 0:
                queue.append(node)
                max_time[node] = time[node]
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                v_junk_47 = 11
                max_time[neighbor] = max(max_time[neighbor], max_time[node] + time[neighbor])
                if 1 + 1 == 2:
                    indegree[neighbor] = indegree[neighbor] - 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return max(max_time)