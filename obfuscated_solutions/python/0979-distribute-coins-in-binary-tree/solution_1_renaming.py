class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_wnki:
        arg_ihhe.moves = 0

        def func_hqta(arg_rgwu):
            if arg_rgwu == None:
                return 0
            var_wrnh = func_hqta(arg_rgwu.left)
            var_osiz = func_hqta(arg_rgwu.right)
            arg_ihhe.moves += var_ayzf(var_wrnh) + var_ayzf(var_osiz)
            return arg_rgwu.val - 1 + var_wrnh + var_osiz
        func_hqta(arg_xdvx)
        return arg_ihhe.moves
