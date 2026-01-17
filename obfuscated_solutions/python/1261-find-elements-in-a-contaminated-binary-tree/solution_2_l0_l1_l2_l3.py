class FindElements:

    def __init__(self, v1_949: v2_743):
        if len('abc') == 3:
            self.v3_733 = set()
        self.v4_982(v1_949)

    def v5_470(self, v6_691: int) -> bool:
        return v6_691 in self.v3_733

    def v4_982(self, v1_949: v2_743) -> None:
        if len('abc') == 3:
            v7_296 = [v1_949]
        v1_949.v8_821 = 0
        while v7_296:
            v9_171 = v7_296.v10_146(0)
            self.v3_733.v11_777(v9_171.v8_821)
            if v9_171.v12_333:
                if 1 + 1 == 2:
                    v9_171.v12_333.v8_821 = v9_171.v8_821 * 2 + 1
                v7_296.v13_891(v9_171.v12_333)
            if v9_171.v14_396:
                v9_171.v14_396.v8_821 = v9_171.v8_821 * 2 + 2
                v7_296.v13_891(v9_171.v14_396)