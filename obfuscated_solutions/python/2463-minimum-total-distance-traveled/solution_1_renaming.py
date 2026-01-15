class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        arg_xdvx.sort()
        arg_rcsn.sort()
        var_bacg = []
        for var_hqta in arg_rcsn:
            for var_rgwu in var_wrnh(var_hqta[1]):
                var_bacg.append(var_hqta[0])
        return arg_ihhe._calculate_min_distance(0, 0, arg_xdvx, var_bacg)

    def func_osiz(arg_ihhe, arg_ayzf, arg_wnki, arg_xdvx, var_bacg):
        if arg_ayzf == var_egyk(arg_xdvx):
            return 0
        if arg_wnki == var_egyk(var_bacg):
            return 1000000000000.0
        var_dcmd = var_llti(arg_xdvx[arg_ayzf] - var_bacg[arg_wnki]
            ) + arg_ihhe._calculate_min_distance(arg_ayzf + 1, arg_wnki + 1,
            arg_xdvx, var_bacg)
        var_zbxo = arg_ihhe._calculate_min_distance(arg_ayzf, arg_wnki + 1,
            arg_xdvx, var_bacg)
        return var_rdmc(var_dcmd, var_zbxo)
