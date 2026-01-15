class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        var_wrnh = var_osiz(arg_xdvx) - 1
        while var_rgwu <= var_wrnh:
            var_ayzf = (var_rgwu + var_wrnh) // 2
            if arg_xdvx[var_ayzf] == arg_rcsn:
                return var_ayzf
            elif arg_xdvx[var_ayzf] < arg_rcsn:
                var_rgwu = var_ayzf + 1
            else:
                var_wrnh = var_ayzf - 1
        return -1
