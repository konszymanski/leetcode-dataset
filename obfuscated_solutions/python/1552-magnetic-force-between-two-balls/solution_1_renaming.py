class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = arg_rcsn[0]
        var_rgwu = 1
        for var_wrnh in var_osiz(1, var_ayzf(arg_rcsn)):
            var_wnki = arg_rcsn[var_wrnh]
            if var_wnki - var_hqta >= arg_xdvx:
                var_rgwu += 1
                var_hqta = var_wnki
            if var_rgwu == arg_bacg:
                return True
        return False

    def func_egyk(arg_ihhe, arg_rcsn: var_dcmd[var_llti], arg_bacg: var_llti
        ) ->var_llti:
        var_zbxo = 0
        var_rdmc = var_ayzf(arg_rcsn)
        arg_rcsn.sort()
        var_rjut = 1
        var_lsgw = var_llti(arg_rcsn[-1] / (arg_bacg - 1.0)) + 1
        while var_rjut <= var_lsgw:
            var_cbvh = var_rjut + (var_lsgw - var_rjut) // 2
            if arg_ihhe.can_place_balls(var_cbvh, arg_rcsn, arg_bacg):
                var_zbxo = var_cbvh
                var_rjut = var_cbvh + 1
            else:
                var_lsgw = var_cbvh - 1
        return var_zbxo
