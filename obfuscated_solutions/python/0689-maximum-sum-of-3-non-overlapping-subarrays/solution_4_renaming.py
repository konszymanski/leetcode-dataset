class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = 0
        var_wrnh = [0, arg_rcsn]
        var_osiz = [0, arg_rcsn, arg_rcsn * 2]
        var_ayzf = var_wnki(arg_xdvx[:arg_rcsn])
        var_egyk = var_wnki(arg_xdvx[arg_rcsn:arg_rcsn * 2])
        var_dcmd = var_wnki(arg_xdvx[arg_rcsn * 2:arg_rcsn * 3])
        var_llti = var_ayzf
        var_zbxo = var_ayzf + var_egyk
        var_rdmc = var_ayzf + var_egyk + var_dcmd
        var_rjut = 1
        var_lsgw = arg_rcsn + 1
        var_cbvh = arg_rcsn * 2 + 1
        while var_cbvh <= var_yjch(arg_xdvx) - arg_rcsn:
            var_ayzf = var_ayzf - arg_xdvx[var_rjut - 1] + arg_xdvx[
                var_rjut + arg_rcsn - 1]
            var_egyk = var_egyk - arg_xdvx[var_lsgw - 1] + arg_xdvx[
                var_lsgw + arg_rcsn - 1]
            var_dcmd = var_dcmd - arg_xdvx[var_cbvh - 1] + arg_xdvx[
                var_cbvh + arg_rcsn - 1]
            if var_ayzf > var_llti:
                var_rgwu = var_rjut
                var_llti = var_ayzf
            if var_egyk + var_llti > var_zbxo:
                var_wrnh[0] = var_rgwu
                var_wrnh[1] = var_lsgw
                var_zbxo = var_egyk + var_llti
            if var_dcmd + var_zbxo > var_rdmc:
                var_osiz[0] = var_wrnh[0]
                var_osiz[1] = var_wrnh[1]
                var_osiz[2] = var_cbvh
                var_rdmc = var_dcmd + var_zbxo
            var_rjut += 1
            var_lsgw += 1
            var_cbvh += 1
        return var_osiz
