class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 1
        var_wrnh = var_osiz(var_ayzf)
        for var_wnki in arg_xdvx:
            var_wrnh[var_wnki % arg_rcsn][var_wnki] = var_wrnh[var_wnki %
                arg_rcsn].get(var_wnki, 0) + 1
        for var_egyk in var_wrnh.values():
            var_dcmd, var_llti, var_zbxo, var_rdmc = -arg_rcsn, 1, 1, 0
            for var_wnki, var_rjut in var_lsgw(var_egyk.items()):
                var_cbvh = var_zbxo
                if var_wnki - var_dcmd == arg_rcsn:
                    var_yjch = ((1 << var_rjut) - 1) * var_rdmc
                else:
                    var_yjch = ((1 << var_rjut) - 1) * var_zbxo
                var_llti = var_cbvh + var_yjch
                var_rdmc, var_zbxo = var_zbxo, var_llti
                var_dcmd = var_wnki
            var_rgwu *= var_llti
        return var_rgwu - 1
