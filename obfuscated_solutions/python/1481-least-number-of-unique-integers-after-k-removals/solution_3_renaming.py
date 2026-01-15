class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = {}
        for var_wrnh in arg_xdvx:
            var_rgwu[var_wrnh] = var_rgwu.get(var_wrnh, 0) + 1
        var_osiz = var_ayzf(arg_xdvx)
        var_wnki = [0] * (var_osiz + 1)
        for var_egyk in var_rgwu.values():
            var_wnki[var_egyk] += 1
        var_dcmd = var_ayzf(var_rgwu)
        for var_wrnh in var_llti(1, var_osiz + 1):
            var_zbxo = var_rdmc(arg_rcsn // var_wrnh, var_wnki[var_wrnh])
            arg_rcsn -= var_wrnh * var_zbxo
            var_dcmd -= var_zbxo
            if arg_rcsn < var_wrnh:
                return var_dcmd
        return 0
