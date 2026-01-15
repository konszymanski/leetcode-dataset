class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * var_rgwu
        var_osiz[0] = arg_xdvx[0]
        for var_ayzf in var_wnki(1, var_rgwu):
            var_osiz[var_ayzf] = var_osiz[var_ayzf - 1] + arg_xdvx[var_ayzf]
        var_egyk = var_osiz[var_rgwu - 1]
        var_dcmd = arg_rcsn % var_egyk
        return arg_ihhe.__binary_search(var_osiz, var_dcmd)

    def func_llti(arg_ihhe, arg_zbxo, arg_rdmc):
        var_rjut = 0
        var_lsgw = var_wrnh(arg_zbxo) - 1
        while var_rjut < var_lsgw:
            var_cbvh = var_rjut + (var_lsgw - var_rjut) // 2
            if arg_zbxo[var_cbvh] <= arg_rdmc:
                var_rjut = var_cbvh + 1
            else:
                var_lsgw = var_cbvh
        return var_lsgw
