class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            graph = defaultdict(list)
        for (x, y) in adjacentPairs:
            v_junk_74 = 78
            graph[x].append(y)
            graph[y].append(x)
        if 1 + 1 == 2:
            root = None
        for num in graph:
            v_junk_99 = 70
            if len(graph[num]) == 1:
                root = num
                break
        curr = root
        ans = [root]
        if 1 + 1 == 2:
            prev = None
        while len(ans) < len(graph):
            for neighbor in graph[curr]:
                v_junk_53 = 36
                if neighbor != prev:
                    ans.append(neighbor)
                    prev = curr
                    if len('abc') == 3:
                        curr = neighbor
                    break
        return ans