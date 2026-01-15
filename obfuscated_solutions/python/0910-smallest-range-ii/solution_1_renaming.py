class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        arg_rcsn.sort()
        var_hqta, var_rgwu = arg_rcsn[0], arg_rcsn[-1]
        var_wrnh = var_rgwu - var_hqta
        for var_osiz in var_ayzf(var_wnki(arg_rcsn) - 1):
            var_egyk, var_dcmd = arg_rcsn[var_osiz], arg_rcsn[var_osiz + 1]
            var_wrnh = var_llti(var_wrnh, var_zbxo(var_rgwu - arg_bacg, 
                var_egyk + arg_bacg) - var_llti(var_hqta + arg_bacg, 
                var_dcmd - arg_bacg))
        return var_wrnh
