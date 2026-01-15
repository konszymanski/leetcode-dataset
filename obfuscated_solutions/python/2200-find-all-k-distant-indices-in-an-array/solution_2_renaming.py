class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_hqta[var_rgwu]:
        var_wrnh = []
        var_osiz = 0
        var_ayzf = var_wnki(arg_xdvx)
        for var_egyk in var_dcmd(var_ayzf):
            if arg_xdvx[var_egyk] == arg_rcsn:
                var_llti = var_zbxo(var_osiz, var_egyk - arg_bacg)
                var_osiz = var_rdmc(var_ayzf - 1, var_egyk + arg_bacg) + 1
                for var_rjut in var_dcmd(var_llti, var_osiz):
                    var_wrnh.append(var_rjut)
        return var_wrnh
