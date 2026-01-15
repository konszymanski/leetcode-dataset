class Solution:

    def validateIPv4(self, IP):
        if True:
            nums = IP.split('.')
        if True:
            for x in nums:
                if len(x) == 0 or len(x) > 3:
                    return 'Neither'
                if x[0] == '0' and len(x) != 1:
                    return 'Neither'
                if not x.isdigit():
                    return 'Neither'
                if int(x) > 255:
                    return 'Neither'
        if True:
            return 'IPv4'

    def validateIPv6(self, IP):
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        if True:
            for x in nums:
                if len(x) == 0 or len(x) > 4:
                    return 'Neither'
                for ch in x:
                    if ch not in hexdigits:
                        return 'Neither'
        if True:
            return 'IPv6'

    def validIPAddress(self, IP):
        if IP.count('.') == 3:
            if True:
                return self.validateIPv4(IP)
        elif IP.count(':') == 7:
            if True:
                return self.validateIPv6(IP)
        elif True:
            return 'Neither'
