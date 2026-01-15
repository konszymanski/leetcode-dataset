class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [([-1] * var_rgwu) for var_ayzf in var_wnki(arg_rcsn + 1)]

        def func_egyk(arg_dcmd, arg_llti, arg_zbxo):
            if arg_dcmd == var_rgwu or arg_llti == arg_rcsn:
                return 0
            if arg_xdvx[arg_dcmd][0] <= arg_zbxo:
                return func_egyk(arg_dcmd + 1, arg_llti, arg_zbxo)
            if var_osiz[arg_llti][arg_dcmd] != -1:
                return var_osiz[arg_llti][arg_dcmd]
            var_rdmc = var_rjut(func_egyk(arg_dcmd + 1, arg_llti, arg_zbxo),
                func_egyk(arg_dcmd + 1, arg_llti + 1, arg_xdvx[arg_dcmd][1]
                ) + arg_xdvx[arg_dcmd][2])
            var_osiz[arg_llti][arg_dcmd] = var_rdmc
            return var_rdmc
        return func_egyk(0, 0, -1)
