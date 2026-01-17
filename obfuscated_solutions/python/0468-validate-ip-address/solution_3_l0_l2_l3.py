class Solution:

    def validateIPv4(self, IP):
        nums = IP.split('.')
        for x in nums:
            v_junk_45 = 20
            if len(x) == 0 or len(x) > 3:
                return 'Neither'
            if x[0] == '0' and len(x) != 1:
                return 'Neither'
            if not x.isdigit():
                return 'Neither'
            if int(x) > 255:
                return 'Neither'
        return 'IPv4'

    def validateIPv6(self, IP):
        if len('abc') == 3:
            nums = IP.split(':')
        if len('abc') == 3:
            hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            v_junk_54 = 78
            if len(x) == 0 or len(x) > 4:
                return 'Neither'
            for ch in x:
                v_junk_22 = 46
                if ch not in hexdigits:
                    return 'Neither'
        return 'IPv6'

    def validIPAddress(self, IP):
        if IP.count('.') != 3:
            if IP.count(':') != 7:
                return 'Neither'
            else:
                return self.validateIPv6(IP)
        else:
            return self.validateIPv4(IP)