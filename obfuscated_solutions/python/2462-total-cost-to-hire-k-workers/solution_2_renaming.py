class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = []
        for var_osiz in var_ayzf(arg_bacg):
            var_wrnh.append((arg_xdvx[var_osiz], 0))
        for var_osiz in var_ayzf(var_wnki(arg_bacg, var_egyk(arg_xdvx) -
            arg_bacg), var_egyk(arg_xdvx)):
            var_wrnh.append((arg_xdvx[var_osiz], 1))
        var_dcmd(var_wrnh)
        var_llti = 0
        var_zbxo, var_rdmc = arg_bacg, var_egyk(arg_xdvx) - 1 - arg_bacg
        for var_rjut in var_ayzf(arg_rcsn):
            var_lsgw, var_cbvh = var_yjch(var_wrnh)
            var_llti += var_lsgw
            if var_zbxo <= var_rdmc:
                if var_cbvh == 0:
                    var_dmio(var_wrnh, (arg_xdvx[var_zbxo], 0))
                    var_zbxo += 1
                else:
                    var_dmio(var_wrnh, (arg_xdvx[var_rdmc], 1))
                    var_rdmc -= 1
        return var_llti
