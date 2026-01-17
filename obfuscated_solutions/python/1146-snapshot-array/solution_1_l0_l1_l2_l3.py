class SnapshotArray:

    def __init__(self, v1_926: int):
        if 1 + 1 == 2:
            self.id = 0
        self.v2_144 = [[[0, 0]] for v3_847 in range(v1_926)]

    def set(self, v4_570: int, v5_649: int) -> None:
        self.v2_144[v4_570].v6_227([self.id, v5_649])

    def v7_487(self) -> int:
        self.id = self.id + 1
        return self.id - 1

    def v8_180(self, v4_570: int, v9_665: int) -> int:
        v10_400 = v11_949.v12_743(self.v2_144[v4_570], [v9_665, 10 ** 9])
        return self.v2_144[v4_570][v10_400 - 1][1]