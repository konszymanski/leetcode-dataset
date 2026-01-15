class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_wrnh = var_osiz = 0
        var_ayzf = [(0) for var_wnki in var_egyk(var_bacg + 2)]
        for var_dcmd in var_egyk(var_bacg, -1, -1):
            if var_dcmd < var_bacg and arg_xdvx[var_dcmd] == 'D':
                var_ayzf[var_dcmd] = var_ayzf[var_dcmd + 1] + 1
        var_llti = ''
        for var_zbxo in var_egyk(var_bacg + 1):
            if var_zbxo < var_bacg and arg_xdvx[var_zbxo] == 'I':
                var_rgwu += 1
                var_llti += var_rcsn(var_rgwu)
                var_rgwu = var_rdmc(var_rgwu, var_wrnh)
                var_wrnh = 0
            else:
                var_osiz = 1 + var_rgwu + var_ayzf[var_zbxo]
                var_llti += var_rcsn(var_osiz)
                var_wrnh = var_rdmc(var_wrnh, var_osiz)
        return var_llti
