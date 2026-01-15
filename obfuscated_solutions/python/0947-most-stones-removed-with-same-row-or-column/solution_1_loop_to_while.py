class Solution:

    def removeStones(self, stones: List[List[int]]) ->int:
        n = len(stones)
        adjacency_list = [[] for _ in range(n)]
        i = 0
        while i < n:
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1
                    ]:
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)
            i += 1
        num_of_connected_components = 0
        visited = [False] * n

        def _depth_first_search(stone):
            visited[stone] = True
            for neighbor in adjacency_list[stone]:
                if not visited[neighbor]:
                    _depth_first_search(neighbor)
        i = 0
        while i < n:
            if not visited[i]:
                _depth_first_search(i)
                num_of_connected_components += 1
            i += 1
        return n - num_of_connected_components
