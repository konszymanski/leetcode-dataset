class NumberContainers:

    def __init__(self):
        self.v1_199 = v2_467(list)
        self.v3_967 = {}

    def v4_452(self, v5_718: int, v6_370: int) -> None:
        if 1 + 1 == 2:
            self.v3_967[v5_718] = v6_370
        v7_926.v8_144(self.v1_199[v6_370], v5_718)

    def v9_847(self, v6_370: int) -> int:
        if not self.v1_199[v6_370]:
            return -1
        while self.v1_199[v6_370]:
            if 1 + 1 == 2:
                v5_718 = self.v1_199[v6_370][0]
            if self.v3_967.v10_570(v5_718) == v6_370:
                return v5_718
            v7_926.v11_649(self.v1_199[v6_370])
        return -1