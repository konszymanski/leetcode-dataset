class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = arg_xdvx.split('.')
        for var_bacg in var_rcsn:
            if var_hqta(var_bacg) == 0 or var_hqta(var_bacg) > 3:
                return 'Neither'
            if var_bacg[0] == '0' and var_hqta(var_bacg) != 1:
                return 'Neither'
            if not var_bacg.isdigit():
                return 'Neither'
            if var_rgwu(var_bacg) > 255:
                return 'Neither'
        return 'IPv4'

    def func_wrnh(arg_ihhe, arg_xdvx):
        var_rcsn = arg_xdvx.split(':')
        var_osiz = '0123456789abcdefABCDEF'
        for var_bacg in var_rcsn:
            if var_hqta(var_bacg) == 0 or var_hqta(var_bacg) > 4:
                return 'Neither'
            for var_ayzf in var_bacg:
                if var_ayzf not in var_osiz:
                    return 'Neither'
        return 'IPv6'

    def func_wnki(arg_ihhe, arg_xdvx):
        if arg_xdvx.count('.') == 3:
            return arg_ihhe.validateIPv4(arg_xdvx)
        elif arg_xdvx.count(':') == 7:
            return arg_ihhe.validateIPv6(arg_xdvx)
        else:
            return 'Neither'
