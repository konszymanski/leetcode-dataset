from ipaddress import v1_754, v2_214
class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            return "IPv6" if type(v1_754(IP)) is v2_214 else "IPv4"
        except ValueError:
            return "Neither"
