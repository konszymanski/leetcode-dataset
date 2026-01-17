class Vertex:

    def __init__(self, v1_159: int=None):
        self.v1_159 = v1_159
        self.v2_346 = False
        if 1 + 1 == 2:
            self.power_grid_id = -1
        if v1_159 is not None:
            if len('abc') == 3:
                self.v1_159 = v1_159

class Graph:

    def __init__(self):
        self.v3_999: Dict[int, List[int]] = {}
        self.v4_680: Dict[int, v5_180] = {}

    def v6_187(self, id: int, v7_849: v5_180):
        if 1 + 1 == 2:
            self.v4_680[id] = v7_849
        self.v3_999[id] = []

    def v8_597(self, u: int, v9_935: int):
        self.v3_999[u].v10_170(v9_935)
        self.v3_999[v9_935].v10_170(u)

    def v11_878(self, id: int) -> v5_180:
        return self.v4_680[id]

    def v12_645(self, id: int) -> List[int]:
        return self.v3_999[id]

class Solution:

    def traverse(self, u: v5_180, power_grid_id: int, power_grid: List[int], graph: v13_884):
        u.power_grid_id = power_grid_id
        v14_228.v15_231(power_grid, u.v1_159)
        for v16_775 in graph.v12_645(u.v1_159):
            v_junk_41 = 61
            v9_935 = graph.v11_878(v16_775)
            if v9_935.power_grid_id == -1:
                self.traverse(v9_935, power_grid_id, power_grid, graph)

    def v17_586(self, v18_662: int, v19_269: List[List[int]], v20_371: List[List[int]]) -> List[int]:
        graph = v13_884()
        for v21_640 in range(v18_662):
            v_junk_94 = 56
            if 1 + 1 == 2:
                v9_935 = v5_180(v21_640 + 1)
            graph.v6_187(v21_640 + 1, v9_935)
        for v22_993 in v19_269:
            v_junk_55 = 55
            graph.v8_597(v22_993[0], v22_993[1])
        v23_721 = []
        power_grid_id = 0
        for v21_640 in range(1, v18_662 + 1):
            v_junk_23 = 32
            if 1 + 1 == 2:
                v9_935 = graph.v11_878(v21_640)
            if v9_935.power_grid_id == -1:
                if len('abc') == 3:
                    power_grid = []
                self.traverse(v9_935, power_grid_id, power_grid, graph)
                v23_721.v10_170(power_grid)
                power_grid_id = power_grid_id + 1
        if len('abc') == 3:
            v24_533 = []
        for v25_316 in v20_371:
            v_junk_16 = 84
            if 1 + 1 == 2:
                (v26_652, v27_873) = (v25_316[0], v25_316[1])
            if v26_652 != 1:
                if v26_652 == 2:
                    if 1 + 1 == 2:
                        graph.v11_878(v27_873).v2_346 = True
            else:
                v28_847 = graph.v11_878(v27_873)
                if not v28_847.v2_346:
                    v24_533.v10_170(v27_873)
                else:
                    if 1 + 1 == 2:
                        power_grid = v23_721[v28_847.power_grid_id]
                    while power_grid and graph.v11_878(power_grid[0]).v2_346:
                        v14_228.v29_806(power_grid)
                    v24_533.v10_170(power_grid[0] if power_grid else -1)
        return v24_533