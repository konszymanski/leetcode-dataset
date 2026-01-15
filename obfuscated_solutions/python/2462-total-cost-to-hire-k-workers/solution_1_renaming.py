class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = arg_xdvx[:arg_bacg]
        var_osiz = arg_xdvx[var_ayzf(arg_bacg, var_wnki(arg_xdvx) - arg_bacg):]
        var_egyk(var_wrnh)
        var_egyk(var_osiz)
        var_dcmd = 0
        var_llti, var_zbxo = arg_bacg, var_wnki(arg_xdvx) - 1 - arg_bacg
        for var_rdmc in var_rjut(arg_rcsn):
            if not var_osiz or var_wrnh and var_wrnh[0] <= var_osiz[0]:
                var_dcmd += var_lsgw(var_wrnh)
                if var_llti <= var_zbxo:
                    var_cbvh(var_wrnh, arg_xdvx[var_llti])
                    var_llti += 1
            else:
                var_dcmd += var_lsgw(var_osiz)
                if var_llti <= var_zbxo:
                    var_cbvh(var_osiz, arg_xdvx[var_zbxo])
                    var_zbxo -= 1
        return var_dcmd
