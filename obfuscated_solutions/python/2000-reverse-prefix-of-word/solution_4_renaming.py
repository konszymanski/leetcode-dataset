class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            if var_hqta[var_osiz] == arg_rcsn:
                while var_wrnh < var_osiz:
                    var_hqta[var_osiz], var_hqta[var_wrnh] = var_hqta[var_wrnh
                        ], var_hqta[var_osiz]
                    var_wrnh += 1
                    var_osiz -= 1
                return ''.join(var_hqta)
        return arg_xdvx
