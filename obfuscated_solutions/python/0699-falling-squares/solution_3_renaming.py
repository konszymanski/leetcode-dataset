class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = [0] * var_hqta(var_rgwu)

        def func_wrnh(arg_osiz, arg_ayzf):
            return var_wnki(var_bacg[var_egyk] for var_egyk in var_dcmd(
                arg_osiz, arg_ayzf + 1))

        def func_llti(arg_osiz, arg_ayzf, arg_zbxo):
            for var_egyk in var_dcmd(arg_osiz, arg_ayzf + 1):
                var_bacg[var_egyk] = var_wnki(var_bacg[var_egyk], arg_zbxo)
        var_rdmc = 0
        var_rjut = []
        for var_lsgw, var_cbvh in arg_rcsn:
            arg_osiz = var_rgwu[var_lsgw]
            arg_ayzf = var_rgwu[var_lsgw + var_cbvh - 1]
            arg_zbxo = func_wrnh(arg_osiz, arg_ayzf) + var_cbvh
            update(arg_osiz, arg_ayzf, arg_zbxo)
            var_rdmc = var_wnki(var_rdmc, arg_zbxo)
            var_rjut.append(var_rdmc)
        return var_rjut
