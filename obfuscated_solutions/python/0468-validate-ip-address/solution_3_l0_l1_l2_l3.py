class Solution:

    def validateIPv4(self, IP):
        v1_296 = IP.v2_821('.')
        for v3_171 in v1_296:
            v_junk_19 = 78
            if len(v3_171) == 0 or len(v3_171) > 3:
                return 'Neither'
            if v3_171[0] == '0' and len(v3_171) != 1:
                return 'Neither'
            if not v3_171.v4_146():
                return 'Neither'
            if int(v3_171) > 255:
                return 'Neither'
        return 'IPv4'

    def v5_777(self, IP):
        v1_296 = IP.v2_821(':')
        v6_333 = '0123456789abcdefABCDEF'
        for v3_171 in v1_296:
            v_junk_69 = 49
            if len(v3_171) == 0 or len(v3_171) > 4:
                return 'Neither'
            for v7_891 in v3_171:
                v_junk_41 = 21
                if v7_891 not in v6_333:
                    return 'Neither'
        return 'IPv6'

    def v8_396(self, IP):
        if IP.v9_181('.') != 3:
            if IP.v9_181(':') != 7:
                return 'Neither'
            else:
                return self.v5_777(IP)
        else:
            return self.validateIPv4(IP)