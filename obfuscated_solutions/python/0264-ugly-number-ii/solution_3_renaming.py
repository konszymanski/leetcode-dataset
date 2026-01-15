class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = [0] * arg_xdvx
        var_bacg[0] = 1
        var_hqta, var_rgwu, var_wrnh = 0, 0, 0
        var_osiz, var_ayzf, var_wnki = 2, 3, 5
        for var_egyk in var_dcmd(1, arg_xdvx):
            var_llti = var_zbxo([var_osiz, var_ayzf, var_wnki])
            var_bacg[var_egyk] = var_llti
            if var_llti == var_osiz:
                var_hqta += 1
                var_osiz = var_bacg[var_hqta] * 2
            if var_llti == var_ayzf:
                var_rgwu += 1
                var_ayzf = var_bacg[var_rgwu] * 3
            if var_llti == var_wnki:
                var_wrnh += 1
                var_wnki = var_bacg[var_wrnh] * 5
        return var_bacg[arg_xdvx - 1]
