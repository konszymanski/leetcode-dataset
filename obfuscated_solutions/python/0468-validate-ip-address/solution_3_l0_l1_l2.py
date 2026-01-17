class Solution:

    def validateIPv4(self, IP):
        v1_754 = IP.v2_214('.')
        for v3_125 in v1_754:
            if len(v3_125) == 0 or len(v3_125) > 3:
                return 'Neither'
            if v3_125[0] == '0' and len(v3_125) != 1:
                return 'Neither'
            if not v3_125.v4_859():
                return 'Neither'
            if int(v3_125) > 255:
                return 'Neither'
        return 'IPv4'

    def v5_381(self, IP):
        v1_754 = IP.v2_214(':')
        v6_350 = '0123456789abcdefABCDEF'
        for v3_125 in v1_754:
            if len(v3_125) == 0 or len(v3_125) > 4:
                return 'Neither'
            for v7_328 in v3_125:
                if v7_328 not in v6_350:
                    return 'Neither'
        return 'IPv6'

    def v8_242(self, IP):
        if IP.v9_854('.') != 3:
            if IP.v9_854(':') != 7:
                return 'Neither'
            else:
                return self.v5_381(IP)
        else:
            return self.validateIPv4(IP)