class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        var_osiz = [([0] * var_hqta) for var_ayzf in var_wnki(var_hqta)]
        var_egyk = {var_dcmd: var_llti for var_llti, var_dcmd in var_zbxo(
            arg_xdvx)}
        for var_rdmc in var_wnki(var_hqta):
            for var_rjut in var_wnki(var_rdmc):
                var_lsgw = arg_xdvx[var_rdmc] - arg_xdvx[var_rjut]
                var_cbvh = var_egyk.get(var_lsgw, -1)
                var_osiz[var_rjut][var_rdmc] = var_osiz[var_cbvh][var_rjut
                    ] + 1 if var_lsgw < arg_xdvx[var_rjut
                    ] and var_cbvh >= 0 else 2
                var_wrnh = var_yjch(var_wrnh, var_osiz[var_rjut][var_rdmc])
        return var_wrnh if var_wrnh > 2 else 0
