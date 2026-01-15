class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        return arg_ihhe._count_beautiful_subsets(arg_xdvx, arg_rcsn, 0, 0)

    def func_bacg(arg_ihhe, arg_xdvx, arg_hqta, arg_rgwu, arg_wrnh):
        if arg_rgwu == var_osiz(arg_xdvx):
            return 1 if arg_wrnh > 0 else 0
        var_ayzf = True
        for var_wnki in var_egyk(arg_rgwu):
            if 1 << var_wnki & arg_wrnh == 0 or var_dcmd(arg_xdvx[var_wnki] -
                arg_xdvx[arg_rgwu]) != arg_hqta:
                continue
            else:
                var_ayzf = False
                break
        var_llti = arg_ihhe._count_beautiful_subsets(arg_xdvx, arg_hqta, 
            arg_rgwu + 1, arg_wrnh)
        var_zbxo = arg_ihhe._count_beautiful_subsets(arg_xdvx, arg_hqta, 
            arg_rgwu + 1, arg_wrnh + (1 << arg_rgwu)) if var_ayzf else 0
        return var_llti + var_zbxo
