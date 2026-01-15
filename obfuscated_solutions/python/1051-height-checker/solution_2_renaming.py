class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta, arg_rgwu):
        var_wrnh = arg_rcsn
        var_osiz = arg_bacg + 1
        var_ayzf = arg_bacg - arg_rcsn + 1
        var_wnki = arg_hqta - arg_bacg
        for var_egyk in var_dcmd(var_ayzf):
            arg_rgwu[var_wrnh + var_egyk] = arg_xdvx[var_wrnh + var_egyk]
        for var_egyk in var_dcmd(var_wnki):
            arg_rgwu[var_osiz + var_egyk] = arg_xdvx[var_osiz + var_egyk]
        var_egyk, var_llti, var_zbxo = 0, 0, arg_rcsn
        while var_egyk < var_ayzf and var_llti < var_wnki:
            if arg_rgwu[var_wrnh + var_egyk] <= arg_rgwu[var_osiz + var_llti]:
                arg_xdvx[var_zbxo] = arg_rgwu[var_wrnh + var_egyk]
                var_egyk += 1
            else:
                arg_xdvx[var_zbxo] = arg_rgwu[var_osiz + var_llti]
                var_llti += 1
            var_zbxo += 1
        while var_egyk < var_ayzf:
            arg_xdvx[var_zbxo] = arg_rgwu[var_wrnh + var_egyk]
            var_egyk += 1
            var_zbxo += 1
        while var_llti < var_wnki:
            arg_xdvx[var_zbxo] = arg_rgwu[var_osiz + var_llti]
            var_llti += 1
            var_zbxo += 1

    def func_rdmc(arg_ihhe, arg_xdvx, arg_rcsn, arg_hqta, arg_rgwu):
        if arg_rcsn >= arg_hqta:
            return
        arg_bacg = (arg_rcsn + arg_hqta) // 2
        arg_ihhe.merge_sort(arg_xdvx, arg_rcsn, arg_bacg, arg_rgwu)
        arg_ihhe.merge_sort(arg_xdvx, arg_bacg + 1, arg_hqta, arg_rgwu)
        arg_ihhe.merge(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta, arg_rgwu)

    def func_rjut(arg_ihhe, arg_lsgw: var_cbvh[var_yjch]) ->var_yjch:
        var_dmio = arg_lsgw[:]
        arg_rgwu = [0] * var_ulfl(arg_lsgw)
        arg_ihhe.merge_sort(var_dmio, 0, var_ulfl(var_dmio) - 1, arg_rgwu)
        var_lgvi = 0
        for var_egyk in var_dcmd(var_ulfl(var_dmio)):
            if arg_lsgw[var_egyk] != var_dmio[var_egyk]:
                var_lgvi += 1
        return var_lgvi
