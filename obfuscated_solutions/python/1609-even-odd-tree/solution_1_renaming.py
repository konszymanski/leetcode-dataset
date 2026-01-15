class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_egyk:
        var_hqta = []

        def func_rgwu(arg_wrnh: var_bacg, arg_osiz: var_ayzf) ->var_egyk:
            if arg_wrnh is None:
                return True
            if arg_wrnh.val % 2 == arg_osiz % 2:
                return False
            while var_wnki(var_hqta) <= arg_osiz:
                var_hqta.append(0)
            if var_hqta[arg_osiz] != 0 and (arg_osiz % 2 == 0 and arg_wrnh.
                val <= var_hqta[arg_osiz] or arg_osiz % 2 == 1 and arg_wrnh
                .val >= var_hqta[arg_osiz]):
                return False
            var_hqta[arg_osiz] = arg_wrnh.val
            return func_rgwu(arg_wrnh.left, arg_osiz + 1) and func_rgwu(
                arg_wrnh.right, arg_osiz + 1)
        arg_wrnh = arg_xdvx
        return func_rgwu(arg_wrnh, 0)
