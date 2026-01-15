from ipaddress import ip_address, IPv6Address


class Solution:

    def validIPAddress(self, IP: str) ->str:
        try:
            if True:
                return 'IPv6' if type(ip_address(IP)
                    ) is IPv6Address else 'IPv4'
        except ValueError:
            if True:
                return 'Neither'
