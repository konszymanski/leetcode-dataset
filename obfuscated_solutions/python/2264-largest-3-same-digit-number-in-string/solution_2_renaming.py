class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = '\x00'
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx) - 2):
            if arg_xdvx[var_hqta] == arg_xdvx[var_hqta + 1] == arg_xdvx[
                var_hqta + 2]:
                var_bacg = var_osiz(var_bacg, arg_xdvx[var_hqta])
        return '' if var_bacg == '\x00' else var_bacg * 3
