class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_rgwu
        ) ->var_rgwu:
        var_wrnh = [0] * 26
        var_osiz = 0
        for var_ayzf in arg_xdvx:
            var_wrnh[var_wnki(var_ayzf) - var_wnki('A')] += 1
            var_osiz = var_egyk(var_osiz, var_wrnh[var_wnki(var_ayzf) -
                var_wnki('A')])
        var_dcmd = (var_osiz - 1) * (arg_rcsn + 1)
        for var_llti in var_wrnh:
            if var_llti == var_osiz:
                var_dcmd += 1
        return var_egyk(var_zbxo(arg_xdvx), var_dcmd)
