class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        arg_bacg[arg_xdvx] = True
        if arg_xdvx == arg_rcsn:
            return True
        var_rgwu = False
        for var_wrnh in arg_hqta[arg_xdvx]:
            if not arg_bacg[var_wrnh]:
                var_rgwu = var_rgwu or arg_ihhe._is_connected(var_wrnh,
                    arg_rcsn, arg_bacg, arg_hqta)
        return var_rgwu

    def func_osiz(arg_ihhe, arg_ayzf):
        var_wnki = var_egyk(arg_ayzf)
        arg_hqta = [[] for var_dcmd in var_llti(var_wnki)]
        for var_zbxo in arg_ayzf:
            arg_bacg = [False] * var_wnki
            if arg_ihhe._is_connected(var_zbxo[0] - 1, var_zbxo[1] - 1,
                arg_bacg, arg_hqta):
                return var_zbxo
            arg_hqta[var_zbxo[0] - 1].append(var_zbxo[1] - 1)
            arg_hqta[var_zbxo[1] - 1].append(var_zbxo[0] - 1)
        return []
