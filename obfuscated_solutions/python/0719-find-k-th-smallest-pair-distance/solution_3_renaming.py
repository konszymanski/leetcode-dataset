class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        var_ayzf = arg_xdvx[var_rgwu - 1] - arg_xdvx[0]
        while var_osiz < var_ayzf:
            var_wnki = (var_osiz + var_ayzf) // 2
            var_egyk = arg_ihhe._count_pairs_with_max_distance(arg_xdvx,
                var_wnki)
            if var_egyk < arg_rcsn:
                var_osiz = var_wnki + 1
            else:
                var_ayzf = var_wnki
        return var_osiz

    def func_dcmd(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_llti: var_hqta
        ) ->var_hqta:
        var_egyk = 0
        var_rgwu = var_wrnh(arg_xdvx)
        var_zbxo = 0
        for var_rdmc in var_rjut(var_rgwu):
            while arg_xdvx[var_rdmc] - arg_xdvx[var_zbxo] > arg_llti:
                var_zbxo += 1
            var_egyk += var_rdmc - var_zbxo
        return var_egyk
