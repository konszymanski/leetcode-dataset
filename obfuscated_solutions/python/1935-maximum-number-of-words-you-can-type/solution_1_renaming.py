class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_wnki:
        var_hqta = var_rgwu(arg_rcsn)
        var_wrnh = 0
        var_osiz = True
        for var_ayzf in arg_xdvx:
            if var_ayzf == ' ':
                if var_osiz:
                    var_wrnh += 1
                var_osiz = True
            elif var_ayzf in var_hqta:
                var_osiz = False
        if var_osiz:
            var_wrnh += 1
        return var_wrnh
