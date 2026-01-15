class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_zbxo:
        if var_rgwu(arg_xdvx) > var_rgwu(arg_rcsn):
            return arg_ihhe.findMedianSortedArrays(arg_rcsn, arg_xdvx)
        var_wrnh, var_osiz = var_rgwu(arg_xdvx), var_rgwu(arg_rcsn)
        var_ayzf, var_wnki = 0, var_wrnh
        while var_ayzf <= var_wnki:
            var_egyk = (var_ayzf + var_wnki) // 2
            var_dcmd = (var_wrnh + var_osiz + 1) // 2 - var_egyk
            var_llti = var_zbxo('-inf') if var_egyk == 0 else arg_xdvx[
                var_egyk - 1]
            var_rdmc = var_zbxo('inf') if var_egyk == var_wrnh else arg_xdvx[
                var_egyk]
            var_rjut = var_zbxo('-inf') if var_dcmd == 0 else arg_rcsn[
                var_dcmd - 1]
            var_lsgw = var_zbxo('inf') if var_dcmd == var_osiz else arg_rcsn[
                var_dcmd]
            if var_llti <= var_lsgw and var_rjut <= var_rdmc:
                if (var_wrnh + var_osiz) % 2 == 0:
                    return (var_cbvh(var_llti, var_rjut) + var_yjch(
                        var_rdmc, var_lsgw)) / 2
                else:
                    return var_cbvh(var_llti, var_rjut)
            elif var_llti > var_lsgw:
                var_wnki = var_egyk - 1
            else:
                var_ayzf = var_egyk + 1
