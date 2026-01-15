class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(var_wrnh for var_wrnh in arg_rcsn if var_wrnh %
            2 == 0)
        var_osiz = []
        for var_wrnh, var_ayzf in arg_bacg:
            if arg_rcsn[var_ayzf] % 2 == 0:
                var_hqta -= arg_rcsn[var_ayzf]
            arg_rcsn[var_ayzf] += var_wrnh
            if arg_rcsn[var_ayzf] % 2 == 0:
                var_hqta += arg_rcsn[var_ayzf]
            var_osiz.append(var_hqta)
        return var_osiz
