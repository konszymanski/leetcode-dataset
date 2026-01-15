class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:

        def func_rgwu(arg_wrnh, arg_osiz):
            var_ayzf = 0
            var_wnki = var_egyk(arg_osiz) - 1
            while var_ayzf <= var_wnki:
                var_dcmd = var_ayzf + (var_wnki - var_ayzf) // 2
                if arg_osiz[var_dcmd] > arg_wrnh:
                    var_wnki = var_dcmd - 1
                elif arg_osiz[var_dcmd] < arg_wrnh:
                    var_ayzf = var_dcmd + 1
                else:
                    return True
            return False
        if var_egyk(arg_xdvx) > var_egyk(arg_rcsn):
            return arg_ihhe.getCommon(arg_rcsn, arg_xdvx)
        for var_llti in arg_xdvx:
            if func_rgwu(var_llti, arg_rcsn):
                return var_llti
        return -1
