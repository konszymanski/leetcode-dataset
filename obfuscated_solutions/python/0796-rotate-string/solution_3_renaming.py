class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_wrnh:
        if var_hqta(arg_xdvx) != var_hqta(arg_rcsn):
            return False
        var_rgwu = arg_xdvx + arg_xdvx
        return arg_ihhe.kmp_search(var_rgwu, arg_rcsn)

    def func_osiz(arg_ihhe, arg_ayzf: var_bacg, arg_wnki: var_bacg) ->var_wrnh:
        var_egyk = arg_ihhe.compute_lps(arg_wnki)
        var_dcmd = var_llti = 0
        var_zbxo = var_hqta(arg_ayzf)
        var_rdmc = var_hqta(arg_wnki)
        while var_dcmd < var_zbxo:
            if arg_ayzf[var_dcmd] == arg_wnki[var_llti]:
                var_dcmd += 1
                var_llti += 1
                if var_llti == var_rdmc:
                    return True
            elif var_llti > 0:
                var_llti = var_egyk[var_llti - 1]
            else:
                var_dcmd += 1
        return False

    def func_rjut(arg_ihhe, arg_wnki: var_bacg) ->var_yjch:
        var_rdmc = var_hqta(arg_wnki)
        var_egyk = [0] * var_rdmc
        var_lsgw = 0
        var_cbvh = 1
        while var_cbvh < var_rdmc:
            if arg_wnki[var_cbvh] == arg_wnki[var_lsgw]:
                var_lsgw += 1
                var_egyk[var_cbvh] = var_lsgw
                var_cbvh += 1
            elif var_lsgw > 0:
                var_lsgw = var_egyk[var_lsgw - 1]
            else:
                var_egyk[var_cbvh] = 0
                var_cbvh += 1
        return var_egyk
