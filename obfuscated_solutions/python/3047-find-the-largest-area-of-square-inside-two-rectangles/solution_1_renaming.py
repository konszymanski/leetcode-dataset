class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        var_rgwu = 0
        for (var_wrnh, var_osiz), (var_ayzf, var_wnki) in var_egyk(var_dcmd
            (arg_xdvx, arg_rcsn), 2):
            var_llti = var_zbxo(var_osiz[0], var_wnki[0]) - var_rdmc(var_wrnh
                [0], var_ayzf[0])
            var_rjut = var_zbxo(var_osiz[1], var_wnki[1]) - var_rdmc(var_wrnh
                [1], var_ayzf[1])
            var_rgwu = var_rdmc(var_rgwu, var_zbxo(var_llti, var_rjut))
        return var_rgwu * var_rgwu
