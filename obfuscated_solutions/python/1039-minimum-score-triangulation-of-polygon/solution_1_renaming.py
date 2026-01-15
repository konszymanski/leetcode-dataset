class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:

        @var_egyk(None)
        def func_hqta(arg_rgwu, arg_wrnh):
            if arg_rgwu + 2 > arg_wrnh:
                return 0
            if arg_rgwu + 2 == arg_wrnh:
                return values[arg_rgwu] * values[arg_rgwu + 1] * values[
                    arg_wrnh]
            return var_osiz(values[arg_rgwu] * values[var_ayzf] * values[
                arg_wrnh] + func_hqta(arg_rgwu, var_ayzf) + func_hqta(
                var_ayzf, arg_wrnh) for var_ayzf in var_wnki(arg_rgwu + 1,
                arg_wrnh))
        return func_hqta(0, var_dcmd(values) - 1)
