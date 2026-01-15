class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        arg_xdvx.sort()
        var_wrnh = 0
        var_osiz = 0
        for var_ayzf in var_wnki(1, arg_rcsn + 1):
            if var_wrnh < var_egyk(arg_xdvx) and arg_xdvx[var_wrnh
                ] == var_ayzf:
                while var_wrnh < var_egyk(arg_xdvx) and arg_xdvx[var_wrnh
                    ] == var_ayzf:
                    var_wrnh += 1
            else:
                arg_bacg -= var_ayzf
                if arg_bacg >= 0:
                    var_osiz += 1
                else:
                    break
        return var_osiz
