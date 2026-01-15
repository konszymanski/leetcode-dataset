class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta()

        def func_rgwu(arg_wrnh, arg_osiz):
            if not (0 <= arg_wrnh < var_ayzf(arg_rcsn) and 0 <= arg_osiz <
                var_ayzf(arg_rcsn[0]) and (arg_wrnh, arg_osiz) not in
                var_bacg and arg_rcsn[arg_wrnh][arg_osiz]):
                return 0
            var_bacg.add((arg_wrnh, arg_osiz))
            return 1 + func_rgwu(arg_wrnh + 1, arg_osiz) + func_rgwu(
                arg_wrnh - 1, arg_osiz) + func_rgwu(arg_wrnh, arg_osiz - 1
                ) + func_rgwu(arg_wrnh, arg_osiz + 1)
        return var_wnki(func_rgwu(arg_wrnh, arg_osiz) for arg_wrnh in
            var_egyk(var_ayzf(arg_rcsn)) for arg_osiz in var_egyk(var_ayzf(
            arg_rcsn[0])))
