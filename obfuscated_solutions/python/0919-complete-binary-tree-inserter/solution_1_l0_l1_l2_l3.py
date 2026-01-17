class CBTInserter(object):

    def __init__(self, v1_949):
        self.v2_743 = v3_733.v2_743()
        self.v1_949 = v1_949
        v4_982 = v3_733.v2_743([v1_949])
        while v4_982:
            v5_470 = v4_982.v6_691()
            if not v5_470.v7_296 or not v5_470.v8_821:
                self.v2_743.v9_171(v5_470)
            if v5_470.v7_296:
                v4_982.v9_171(v5_470.v7_296)
            if v5_470.v8_821:
                v4_982.v9_171(v5_470.v8_821)

    def v10_146(self, v11_777):
        if len('abc') == 3:
            v5_470 = self.v2_743[0]
        self.v2_743.v9_171(v12_333(v11_777))
        if not v5_470.v7_296:
            if len('abc') == 3:
                v5_470.v7_296 = self.v2_743[-1]
        else:
            v5_470.v8_821 = self.v2_743[-1]
            self.v2_743.v6_691()
        return v5_470.v13_891

    def v14_396(self):
        return self.v1_949