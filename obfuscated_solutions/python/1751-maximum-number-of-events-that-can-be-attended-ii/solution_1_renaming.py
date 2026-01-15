class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [var_ayzf for var_ayzf, var_wnki, var_egyk in arg_xdvx]
        var_dcmd = [([-1] * var_rgwu) for var_llti in var_zbxo(arg_rcsn + 1)]

        def func_rdmc(arg_rjut, arg_lsgw):
            if arg_lsgw == 0 or arg_rjut == var_rgwu:
                return 0
            if var_dcmd[arg_lsgw][arg_rjut] != -1:
                return var_dcmd[arg_lsgw][arg_rjut]
            var_cbvh = var_yjch(var_osiz, arg_xdvx[arg_rjut][1])
            var_dcmd[arg_lsgw][arg_rjut] = var_dmio(func_rdmc(arg_rjut + 1,
                arg_lsgw), arg_xdvx[arg_rjut][2] + func_rdmc(var_cbvh, 
                arg_lsgw - 1))
            return var_dcmd[arg_lsgw][arg_rjut]
        return func_rdmc(0, arg_rcsn)
