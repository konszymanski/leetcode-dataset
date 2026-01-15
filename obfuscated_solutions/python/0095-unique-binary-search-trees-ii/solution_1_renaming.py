class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = []
        if arg_xdvx > arg_rcsn:
            var_hqta.append(None)
            return var_hqta
        if (arg_xdvx, arg_rcsn) in arg_bacg:
            return arg_bacg[arg_xdvx, arg_rcsn]
        for var_rgwu in var_wrnh(arg_xdvx, arg_rcsn + 1):
            var_osiz = arg_ihhe.allPossibleBST(arg_xdvx, var_rgwu - 1, arg_bacg
                )
            var_ayzf = arg_ihhe.allPossibleBST(var_rgwu + 1, arg_rcsn, arg_bacg
                )
            for var_wnki in var_osiz:
                for var_egyk in var_ayzf:
                    var_dcmd = var_llti(var_rgwu, var_wnki, var_egyk)
                    var_hqta.append(var_dcmd)
        arg_bacg[arg_xdvx, arg_rcsn] = var_hqta
        return var_hqta

    def func_zbxo(arg_ihhe, arg_rdmc: var_rjut) ->var_lsgw[var_cbvh[var_llti]]:
        arg_bacg = {}
        return arg_ihhe.allPossibleBST(1, arg_rdmc, arg_bacg)
