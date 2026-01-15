class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        if arg_rcsn > 0:
            return var_wrnh(arg_xdvx, arg_bacg // arg_rcsn)
        elif arg_rcsn < 0:
            return var_osiz(arg_xdvx) - var_ayzf(arg_xdvx, -(-arg_bacg //
                arg_rcsn))
        else:
            return var_osiz(arg_xdvx) if arg_bacg >= 0 else 0

    def func_wnki(arg_ihhe, arg_egyk: var_hqta[var_rgwu], arg_xdvx:
        var_hqta[var_rgwu], arg_dcmd: var_rgwu) ->var_rgwu:
        var_llti = var_osiz(arg_egyk)
        var_zbxo, var_rdmc = -10 ** 10, 10 ** 10
        while var_zbxo <= var_rdmc:
            var_rjut = (var_zbxo + var_rdmc) // 2
            var_lsgw = 0
            for var_cbvh in var_yjch(var_llti):
                var_lsgw += arg_ihhe.f(arg_xdvx, arg_egyk[var_cbvh], var_rjut)
            if var_lsgw < arg_dcmd:
                var_zbxo = var_rjut + 1
            else:
                var_rdmc = var_rjut - 1
        return var_zbxo
