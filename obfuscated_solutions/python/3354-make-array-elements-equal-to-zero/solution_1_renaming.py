class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        var_bacg = var_hqta(1 for var_rgwu in arg_xdvx if var_rgwu > 0)
        var_wrnh = var_osiz(arg_xdvx)
        for var_ayzf in var_wnki(var_wrnh):
            if arg_xdvx[var_ayzf] == 0:
                if arg_ihhe.isValid(arg_xdvx, var_bacg, var_ayzf, -1):
                    var_rcsn += 1
                if arg_ihhe.isValid(arg_xdvx, var_bacg, var_ayzf, 1):
                    var_rcsn += 1
        return var_rcsn

    def func_egyk(arg_ihhe, arg_xdvx, var_bacg, arg_dcmd, arg_llti):
        var_zbxo = arg_xdvx[:]
        var_rdmc = arg_dcmd
        while var_bacg > 0 and 0 <= var_rdmc < var_osiz(arg_xdvx):
            if var_zbxo[var_rdmc] > 0:
                var_zbxo[var_rdmc] -= 1
                arg_llti *= -1
                if var_zbxo[var_rdmc] == 0:
                    var_bacg -= 1
            var_rdmc += arg_llti
        return var_bacg == 0
