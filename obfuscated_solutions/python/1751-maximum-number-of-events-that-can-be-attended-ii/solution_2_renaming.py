class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [([0] * (var_rgwu + 1)) for var_ayzf in var_wnki(
            arg_rcsn + 1)]
        arg_xdvx.sort()
        var_egyk = [var_dcmd for var_dcmd, var_llti, var_zbxo in arg_xdvx]
        for var_rdmc in var_wnki(var_rgwu - 1, -1, -1):
            for var_rjut in var_wnki(1, arg_rcsn + 1):
                var_lsgw = var_cbvh(var_egyk, arg_xdvx[var_rdmc][1])
                var_osiz[var_rjut][var_rdmc] = var_yjch(var_osiz[var_rjut][
                    var_rdmc + 1], arg_xdvx[var_rdmc][2] + var_osiz[
                    var_rjut - 1][var_lsgw])
        return var_osiz[arg_rcsn][0]
