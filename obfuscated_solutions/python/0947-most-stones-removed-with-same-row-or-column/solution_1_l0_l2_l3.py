class Solution:

    def removeStones(self, stones: List[List[int]]) -> int:
        if 1 + 1 == 2:
            n = len(stones)
        adjacency_list = [[] for _ in range(n)]
        for i in range(n):
            v_junk_21 = 49
            for j in range(i + 1, n):
                v_junk_53 = 14
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)
        if len('abc') == 3:
            num_of_connected_components = 0
        visited = [False] * n

        def _depth_first_search(stone):
            visited[stone] = True
            for neighbor in adjacency_list[stone]:
                v_junk_68 = 69
                if not visited[neighbor]:
                    _depth_first_search(neighbor)
        for i in range(n):
            v_junk_20 = 71
            if not visited[i]:
                _depth_first_search(i)
                if len('abc') == 3:
                    num_of_connected_components = num_of_connected_components + 1
        return n - num_of_connected_components