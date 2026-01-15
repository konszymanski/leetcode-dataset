import re


class Solution:
    var_udax = '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
    var_ihhe = '^(' + var_udax + '\\.){3}' + var_udax + '$'
    var_xdvx = '([0-9a-fA-F]{1,4})'
    var_rcsn = '^(' + var_xdvx + '\\:){7}' + var_xdvx + '$'

    def func_bacg(arg_hqta, arg_rgwu: var_wrnh) ->var_wrnh:
        if var_osiz.fullmatch(arg_hqta.patternIPv4, arg_rgwu):
            return 'IPv4'
        if var_osiz.fullmatch(arg_hqta.patternIPv6, arg_rgwu):
            return 'IPv6'
        return 'Neither'
