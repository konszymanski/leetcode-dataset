class FindElements:

    def __init__(self, v1_818: v2_658):
        self.v3_529 = set()
        self.v4_325(v1_818, 0)

    def v5_559(self, v6_703: int) -> bool:
        return v6_703 in self.v3_529

    def v4_325(self, v7_384, v8_928):
        if v7_384 is None:
            return
        self.v3_529.v9_990(v8_928)
        self.v4_325(v7_384.v10_106, v8_928 * 2 + 1)
        self.v4_325(v7_384.v11_877, v8_928 * 2 + 2)