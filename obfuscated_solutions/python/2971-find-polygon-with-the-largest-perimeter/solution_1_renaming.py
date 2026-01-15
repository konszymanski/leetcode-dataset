class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        arg_xdvx.sort()
        var_hqta = 0
        var_rgwu = -1
        for var_wrnh in arg_xdvx:
            if var_wrnh < var_hqta:
                var_rgwu = var_wrnh + var_hqta
            var_hqta += var_wrnh
        return var_rgwu
