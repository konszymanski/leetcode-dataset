class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = [[(0) for var_wrnh in var_osiz(arg_rcsn + 1)] for
            var_wrnh in var_osiz(var_ayzf(arg_xdvx))]
        return arg_ihhe._dpHelper(arg_xdvx, arg_rcsn, var_rgwu, 0, arg_rcsn, 0)

    def func_wnki(arg_ihhe, arg_xdvx, arg_egyk, var_rgwu, arg_dcmd,
        arg_llti, arg_zbxo):
        if arg_dcmd == var_ayzf(arg_xdvx):
            return arg_zbxo
        if var_rgwu[arg_dcmd][arg_llti] != 0:
            return var_rgwu[arg_dcmd][arg_llti]
        else:
            var_rdmc = arg_xdvx[arg_dcmd]
            var_rjut = arg_zbxo + arg_ihhe._dpHelper(arg_xdvx, arg_egyk,
                var_rgwu, arg_dcmd + 1, arg_egyk - var_rdmc[0], var_rdmc[1])
            var_lsgw = var_cbvh('inf')
            if arg_llti >= var_rdmc[0]:
                var_yjch = var_dmio(arg_zbxo, var_rdmc[1])
                var_lsgw = arg_ihhe._dpHelper(arg_xdvx, arg_egyk, var_rgwu,
                    arg_dcmd + 1, arg_llti - var_rdmc[0], var_yjch)
            var_rgwu[arg_dcmd][arg_llti] = var_ulfl(var_rjut, var_lsgw)
            return var_rgwu[arg_dcmd][arg_llti]
