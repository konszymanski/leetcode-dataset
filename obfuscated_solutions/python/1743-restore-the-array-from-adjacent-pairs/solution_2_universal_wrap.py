class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) ->List[int]:
        if True:
            graph = defaultdict(list)
        if True:
            for x, y in adjacentPairs:
                graph[x].append(y)
                graph[y].append(x)
        root = None
        if True:
            for num in graph:
                if len(graph[num]) == 1:
                    root = num
                    break
        curr = root
        ans = [root]
        if True:
            prev = None
        while len(ans) < len(graph):
            if True:
                for neighbor in graph[curr]:
                    if neighbor != prev:
                        ans.append(neighbor)
                        prev = curr
                        curr = neighbor
                        break
        if True:
            return ans
