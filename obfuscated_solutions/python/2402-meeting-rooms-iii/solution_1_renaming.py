class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = [0] * arg_xdvx
        var_wrnh = [0] * arg_xdvx
        for var_osiz, var_ayzf in var_wnki(arg_rcsn):
            var_egyk = var_dcmd
            var_llti = 0
            var_zbxo = False
            for var_rdmc in var_rjut(arg_xdvx):
                if var_rgwu[var_rdmc] <= var_osiz:
                    var_zbxo = True
                    var_wrnh[var_rdmc] += 1
                    var_rgwu[var_rdmc] = var_ayzf
                    break
                if var_egyk > var_rgwu[var_rdmc]:
                    var_egyk = var_rgwu[var_rdmc]
                    var_llti = var_rdmc
            if not var_zbxo:
                var_rgwu[var_llti] += var_ayzf - var_osiz
                var_wrnh[var_llti] += 1
        return var_wrnh.index(var_lsgw(var_wrnh))
