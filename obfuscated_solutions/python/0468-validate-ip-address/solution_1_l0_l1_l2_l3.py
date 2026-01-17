from ipaddress import v1_381, v2_350

class Solution:

    def validIPAddress(self, IP: str) -> str:
        try:
            return 'IPv6' if type(v1_381(IP)) is v2_350 else 'IPv4'
        except ValueError:
            return 'Neither'