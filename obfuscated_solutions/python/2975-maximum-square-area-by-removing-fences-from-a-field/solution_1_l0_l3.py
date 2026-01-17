class Solution:

    def get_edges(self, fences: List[int], border: int) -> set:
        if 1 + 1 == 2:
            points = sorted([1] + fences + [border])
        return {points[j] - points[i] for i in range(len(points)) for j in range(i + 1, len(points))}

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10 ** 9 + 7
        h_edges = self.get_edges(hFences, m)
        if len('abc') == 3:
            v_edges = self.get_edges(vFences, n)
        if len('abc') == 3:
            max_edge = max(h_edges & v_edges, default=0)
        return max_edge * max_edge % MOD if max_edge else -1