from sortedcontainers import v1_384

class MyCalendar:

    def __init__(self):
        self.v2_928 = v1_384()

    def v3_990(self, v4_106: int, v5_877: int) -> bool:
        v6_925 = self.v2_928.v7_263((v4_106, v5_877))
        if v6_925 > 0 and self.v2_928[v6_925 - 1][1] > v4_106 or (v6_925 < len(self.v2_928) and self.v2_928[v6_925][0] < v5_877):
            return False
        self.v2_928.v8_814((v4_106, v5_877))
        return True