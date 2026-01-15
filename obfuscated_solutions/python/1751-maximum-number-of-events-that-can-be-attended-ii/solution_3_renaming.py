class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [var_ayzf for var_ayzf, var_wnki, var_egyk in arg_xdvx]
        var_dcmd = [var_llti(var_osiz, arg_xdvx[var_zbxo][1]) for var_zbxo in
            var_rdmc(var_rgwu)]
        var_rjut = [([-1] * var_rgwu) for var_lsgw in var_rdmc(arg_rcsn)]

        def func_cbvh(var_zbxo, arg_yjch):
            if arg_yjch == arg_rcsn or var_zbxo == var_rgwu:
                return 0
            if var_rjut[arg_yjch][var_zbxo] != -1:
                return var_rjut[arg_yjch][var_zbxo]
            var_dmio = var_dcmd[var_zbxo]
            var_rjut[arg_yjch][var_zbxo] = var_ulfl(func_cbvh(var_zbxo + 1,
                arg_yjch), arg_xdvx[var_zbxo][2] + func_cbvh(var_dmio, 
                arg_yjch + 1))
            return var_rjut[arg_yjch][var_zbxo]
        return func_cbvh(0, 0)
