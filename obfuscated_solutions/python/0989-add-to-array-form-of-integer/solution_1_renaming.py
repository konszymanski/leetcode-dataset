class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        arg_rcsn[-1] += arg_bacg
        for var_hqta in var_rgwu(var_wrnh(arg_rcsn) - 1, -1, -1):
            var_osiz, arg_rcsn[var_hqta] = var_ayzf(arg_rcsn[var_hqta], 10)
            if var_hqta:
                arg_rcsn[var_hqta - 1] += var_osiz
        if var_osiz:
            arg_rcsn = var_wnki(var_egyk, var_dcmd(var_osiz)) + arg_rcsn
        return arg_rcsn
