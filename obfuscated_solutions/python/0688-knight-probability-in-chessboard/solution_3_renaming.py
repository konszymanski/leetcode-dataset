class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu, arg_hqta: var_rgwu) ->var_dmio:
        var_wrnh = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-
            2, 1), (-2, -1)]
        var_osiz = [[([-1] * arg_xdvx) for var_ayzf in var_wnki(arg_xdvx)] for
            var_ayzf in var_wnki(arg_rcsn + 1)]

        def func_egyk(arg_dcmd, arg_llti, arg_zbxo):
            if arg_dcmd == 0:
                if arg_llti == arg_bacg and arg_zbxo == arg_hqta:
                    return 1
                else:
                    return 0
            if var_osiz[arg_dcmd][arg_llti][arg_zbxo] != -1:
                return var_osiz[arg_dcmd][arg_llti][arg_zbxo]
            var_osiz[arg_dcmd][arg_llti][arg_zbxo] = 0
            for var_rdmc in var_wrnh:
                var_rjut = arg_llti - var_rdmc[0]
                var_lsgw = arg_zbxo - var_rdmc[1]
                if 0 <= var_rjut < arg_xdvx and 0 <= var_lsgw < arg_xdvx:
                    var_osiz[arg_dcmd][arg_llti][arg_zbxo] += func_egyk(
                        arg_dcmd - 1, var_rjut, var_lsgw)
            var_osiz[arg_dcmd][arg_llti][arg_zbxo] /= 8
            return var_osiz[arg_dcmd][arg_llti][arg_zbxo]
        var_cbvh = var_yjch(func_egyk(arg_rcsn, arg_llti, arg_zbxo) for
            arg_llti in var_wnki(arg_xdvx) for arg_zbxo in var_wnki(arg_xdvx))
        return var_cbvh
