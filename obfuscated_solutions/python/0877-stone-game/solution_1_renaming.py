from functools import lru_cache


class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)

        @var_egyk(None)
        def func_hqta(arg_rgwu, arg_wrnh):
            if arg_rgwu > arg_wrnh:
                return 0
            var_osiz = (arg_wrnh - arg_rgwu - var_rcsn) % 2
            if var_osiz == 1:
                return var_ayzf(arg_xdvx[arg_rgwu] + func_hqta(arg_rgwu + 1,
                    arg_wrnh), arg_xdvx[arg_wrnh] + func_hqta(arg_rgwu, 
                    arg_wrnh - 1))
            else:
                return var_wnki(-arg_xdvx[arg_rgwu] + func_hqta(arg_rgwu + 
                    1, arg_wrnh), -arg_xdvx[arg_wrnh] + func_hqta(arg_rgwu,
                    arg_wrnh - 1))
        return func_hqta(0, var_rcsn - 1) > 0
