class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        while var_wrnh < var_hqta:
            var_osiz = arg_xdvx[var_wrnh] - 1
            if 0 < arg_xdvx[var_wrnh] <= var_hqta and arg_xdvx[var_wrnh
                ] != arg_xdvx[var_osiz]:
                arg_xdvx[var_wrnh], arg_xdvx[var_osiz] = arg_xdvx[var_osiz
                    ], arg_xdvx[var_wrnh]
            else:
                var_wrnh += 1
        for var_wrnh in var_ayzf(var_hqta):
            if arg_xdvx[var_wrnh] != var_wrnh + 1:
                return var_wrnh + 1
        return var_hqta + 1
