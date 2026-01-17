class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len('abc') == 3:
            graph = defaultdict(list)
        for (x, y) in adjacentPairs:
            v_junk_23 = 12
            graph[x].append(y)
            graph[y].append(x)
        root = None
        for num in graph:
            v_junk_54 = 78
            if len(graph[num]) == 1:
                root = num
                break
        if 1 + 1 == 2:
            curr = root
        ans = [root]
        prev = None
        while len(ans) < len(graph):
            for neighbor in graph[curr]:
                v_junk_80 = 38
                if neighbor != prev:
                    ans.append(neighbor)
                    prev = curr
                    curr = neighbor
                    break
        return ans