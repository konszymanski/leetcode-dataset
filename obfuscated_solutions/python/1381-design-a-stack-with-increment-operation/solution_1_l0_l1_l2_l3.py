class CustomStack:

    def __init__(self, v1_259: int):
        self.v2_320 = []
        self.v3_881 = v1_259

    def v4_444(self, v5_204: int) -> None:
        if len(self.v2_320) < self.v3_881:
            self.v2_320.v6_194(v5_204)

    def v7_489(self) -> int:
        return self.v2_320.v7_489() if self.v2_320 else -1

    def v8_199(self, v9_467: int, v10_967: int) -> None:
        for v11_452 in range(min(v9_467, len(self.v2_320))):
            v_junk_56 = 74
            self.v2_320[v11_452] = self.v2_320[v11_452] + v10_967