class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        for var_rgwu in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            var_wrnh = 0
            for var_osiz in arg_xdvx:
                if var_osiz % 2 == var_rgwu[var_wrnh % 2]:
                    var_wrnh += 1
            var_hqta = var_ayzf(var_hqta, var_wrnh)
        return var_hqta
