import re

class Solution:
    v1_821 = '([0-9]|[1-9][0-9] | 1[0-9]{2}|2[0-4][0-9] | 25[0 - 5])'
    if 1 + 1 == 2:
        v2_171 = ' ^ (' + v1_821 + '\\.){3}' + v1_821 + '$'
    v3_146 = '([0 - 9a - fA - F]{1,4})'
    v4_777 = ' ^ (' + v3_146 + '\\:){7}' + v3_146 + '$'

    def validIPAddress(self, IP: str) -> str:
        if v5_333.v6_891(self.v2_171, IP):
            return 'IPv4'
        if v5_333.v6_891(self.v4_777, IP):
            return 'IPv6'
        return 'Neither'