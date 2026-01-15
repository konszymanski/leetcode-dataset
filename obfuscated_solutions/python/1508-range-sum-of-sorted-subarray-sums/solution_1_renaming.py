class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu[var_wrnh], arg_rcsn:
        var_wrnh, arg_bacg: var_wrnh, arg_hqta: var_wrnh) ->var_wrnh:
        var_osiz = []
        for var_ayzf in var_wnki(var_egyk(arg_xdvx)):
            var_dcmd = 0
            for var_llti in var_wnki(var_ayzf, var_egyk(arg_xdvx)):
                var_dcmd += arg_xdvx[var_llti]
                var_osiz.append(var_dcmd)
        var_osiz.sort()
        var_zbxo = 0
        var_rdmc = 10 ** 9 + 7
        for var_ayzf in var_wnki(arg_bacg - 1, arg_hqta):
            var_zbxo = (var_zbxo + var_osiz[var_ayzf]) % var_rdmc
        return var_zbxo
