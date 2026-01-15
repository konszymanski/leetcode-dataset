class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:

        def func_hqta(arg_xdvx: var_rcsn[var_bacg], arg_rgwu: var_bacg,
            arg_wrnh: var_bacg) ->var_bacg:
            if arg_rgwu == var_osiz(arg_xdvx):
                return arg_wrnh
            var_ayzf = func_hqta(arg_xdvx, arg_rgwu + 1, arg_wrnh ^
                arg_xdvx[arg_rgwu])
            var_wnki = func_hqta(arg_xdvx, arg_rgwu + 1, arg_wrnh)
            return var_ayzf + var_wnki
        return func_hqta(arg_xdvx, 0, 0)
