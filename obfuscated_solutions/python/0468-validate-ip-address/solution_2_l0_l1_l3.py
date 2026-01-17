import re

class Solution:
    v1_754 = '([0 - 9] | [1 - 9][0-9]|1[0-9]{2}|2[0 - 4][0-9]|25[0 - 5])'
    v2_214 = ' ^ (' + v1_754 + '\\.){3}' + v1_754 + '$'
    v3_125 = '([0 - 9a - fA-F]{1,4})'
    v4_859 = '^(' + v3_125 + '\\:){7}' + v3_125 + '$'

    def validIPAddress(self, IP: str) -> str:
        if v5_381.v6_350(self.v2_214, IP):
            return 'IPv4'
        if v5_381.v6_350(self.v4_859, IP):
            return 'IPv6'
        return 'Neither'