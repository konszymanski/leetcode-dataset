class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_bacg[var_zbxo]:
        var_rgwu = [False] * var_wrnh(arg_rcsn)
        var_osiz = [0] * var_wrnh(arg_xdvx)
        var_osiz[0] = 0
        for var_ayzf in var_wnki(1, var_wrnh(arg_xdvx)):
            if arg_xdvx[var_ayzf] % 2 == arg_xdvx[var_ayzf - 1] % 2:
                var_osiz[var_ayzf] = var_osiz[var_ayzf - 1] + 1
            else:
                var_osiz[var_ayzf] = var_osiz[var_ayzf - 1]
        for var_ayzf in var_wnki(var_wrnh(arg_rcsn)):
            var_egyk = arg_rcsn[var_ayzf]
            var_dcmd = var_egyk[0]
            var_llti = var_egyk[1]
            var_rgwu[var_ayzf] = var_osiz[var_llti] - var_osiz[var_dcmd] == 0
        return var_rgwu
