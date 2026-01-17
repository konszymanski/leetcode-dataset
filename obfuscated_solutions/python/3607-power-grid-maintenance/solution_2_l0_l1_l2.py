class Vertex:

    def __init__(self, v1_754: int=None):
        self.v1_754 = v1_754
        self.v2_214 = False
        self.power_grid_id = -1
        if v1_754 is not None:
            self.v1_754 = v1_754

class Graph:

    def __init__(self):
        self.v3_125: Dict[int, List[int]] = {}
        self.v4_859: Dict[int, v5_381] = {}

    def v6_350(self, id: int, v7_328: v5_381):
        self.v4_859[id] = v7_328
        self.v3_125[id] = []

    def v8_242(self, u: int, v9_854: int):
        self.v3_125[u].v10_204(v9_854)
        self.v3_125[v9_854].v10_204(u)

    def v11_792(self, id: int) -> v5_381:
        return self.v4_859[id]

    def v12_858(self, id: int) -> List[int]:
        return self.v3_125[id]

class Solution:

    def traverse(self, u: v5_381, power_grid_id: int, power_grid: List[int], graph: v13_658):
        u.power_grid_id = power_grid_id
        v14_189.v15_704(power_grid, u.v1_754)
        for v16_532 in graph.v12_858(u.v1_754):
            v9_854 = graph.v11_792(v16_532)
            if v9_854.power_grid_id == -1:
                self.traverse(v9_854, power_grid_id, power_grid, graph)

    def v17_132(self, v18_130: int, v19_195: List[List[int]], v20_323: List[List[int]]) -> List[int]:
        graph = v13_658()
        for v21_338 in range(v18_130):
            v9_854 = v5_381(v21_338 + 1)
            graph.v6_350(v21_338 + 1, v9_854)
        for v22_617 in v19_195:
            graph.v8_242(v22_617[0], v22_617[1])
        v23_716 = []
        power_grid_id = 0
        for v21_338 in range(1, v18_130 + 1):
            v9_854 = graph.v11_792(v21_338)
            if v9_854.power_grid_id == -1:
                power_grid = []
                self.traverse(v9_854, power_grid_id, power_grid, graph)
                v23_716.v10_204(power_grid)
                power_grid_id = power_grid_id + 1
        v24_127 = []
        for v25_674 in v20_323:
            (v26_303, v27_833) = (v25_674[0], v25_674[1])
            if v26_303 != 1:
                if v26_303 == 2:
                    graph.v11_792(v27_833).v2_214 = True
            else:
                v28_765 = graph.v11_792(v27_833)
                if not v28_765.v2_214:
                    v24_127.v10_204(v27_833)
                else:
                    power_grid = v23_716[v28_765.power_grid_id]
                    while power_grid and graph.v11_792(power_grid[0]).v2_214:
                        v14_189.v29_818(power_grid)
                    v24_127.v10_204(power_grid[0] if power_grid else -1)
        return v24_127