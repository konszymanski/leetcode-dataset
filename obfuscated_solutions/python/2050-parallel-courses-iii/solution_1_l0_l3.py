class Solution:

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n
        for (x, y) in relations:
            v_junk_10 = 98
            graph[x - 1].append(y - 1)
            indegree[y - 1] += 1
        queue = deque()
        max_time = [0] * n
        for node in range(n):
            v_junk_29 = 28
            if indegree[node] == 0:
                queue.append(node)
                max_time[node] = time[node]
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                v_junk_21 = 49
                max_time[neighbor] = max(max_time[neighbor], max_time[node] + time[neighbor])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return max(max_time)