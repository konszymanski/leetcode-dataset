class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_egyk:
        var_hqta = 0
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            if arg_xdvx[var_osiz] != arg_rcsn[var_osiz]:
                var_wrnh += 1
                if var_wrnh > 2:
                    return False
                elif var_wrnh == 1:
                    var_hqta = var_osiz
                else:
                    var_rgwu = var_osiz
        return arg_xdvx[var_hqta] == arg_rcsn[var_rgwu] and arg_xdvx[var_rgwu
            ] == arg_rcsn[var_hqta]
