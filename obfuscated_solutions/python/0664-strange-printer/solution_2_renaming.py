class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_cbvh:
        arg_xdvx = ''.join(var_bacg for var_bacg, var_hqta in var_rgwu.
            groupby(arg_xdvx))
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [([0] * var_wrnh) for var_hqta in var_wnki(var_wrnh)]
        for var_egyk in var_wnki(var_wrnh):
            var_ayzf[var_egyk][var_egyk] = 1
        for var_dcmd in var_wnki(2, var_wrnh + 1):
            for var_llti in var_wnki(var_wrnh - var_dcmd + 1):
                var_zbxo = var_llti + var_dcmd - 1
                var_ayzf[var_llti][var_zbxo] = var_dcmd
                for var_rdmc in var_wnki(var_dcmd - 1):
                    var_rjut = var_ayzf[var_llti][var_llti + var_rdmc
                        ] + var_ayzf[var_llti + var_rdmc + 1][var_zbxo]
                    if arg_xdvx[var_llti + var_rdmc] == arg_xdvx[var_zbxo]:
                        var_rjut -= 1
                    var_ayzf[var_llti][var_zbxo] = var_lsgw(var_ayzf[
                        var_llti][var_zbxo], var_rjut)
        return var_ayzf[0][var_wrnh - 1] if var_wrnh > 0 else 0
