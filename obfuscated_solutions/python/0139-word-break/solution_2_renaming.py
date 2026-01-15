class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_egyk:

        @var_wnki
        def func_rgwu(arg_wrnh):
            if arg_wrnh < 0:
                return True
            for var_osiz in arg_rcsn:
                if arg_xdvx[arg_wrnh - var_ayzf(var_osiz) + 1:arg_wrnh + 1
                    ] == var_osiz and func_rgwu(arg_wrnh - var_ayzf(var_osiz)):
                    return True
            return False
        return func_rgwu(var_ayzf(arg_xdvx) - 1)
