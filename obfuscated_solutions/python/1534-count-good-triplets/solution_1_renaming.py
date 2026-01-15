class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu[var_wrnh], arg_rcsn:
        var_wrnh, arg_bacg: var_wrnh, arg_hqta: var_wrnh) ->var_wrnh:
        var_osiz = var_ayzf(arg_xdvx)
        var_wnki = 0
        for var_egyk in var_dcmd(var_osiz):
            for var_llti in var_dcmd(var_egyk + 1, var_osiz):
                for var_zbxo in var_dcmd(var_llti + 1, var_osiz):
                    if var_rdmc(arg_xdvx[var_egyk] - arg_xdvx[var_llti]
                        ) <= arg_rcsn and var_rdmc(arg_xdvx[var_llti] -
                        arg_xdvx[var_zbxo]) <= arg_bacg and var_rdmc(
                        arg_xdvx[var_egyk] - arg_xdvx[var_zbxo]) <= arg_hqta:
                        var_wnki += 1
        return var_wnki
