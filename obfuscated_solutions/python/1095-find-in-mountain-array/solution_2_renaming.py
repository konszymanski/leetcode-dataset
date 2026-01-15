class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: 'MountainArray'
        ) ->var_bacg:
        var_hqta = arg_rcsn.length()
        var_rgwu = {}
        var_wrnh = 1
        var_osiz = var_hqta - 2
        while var_wrnh != var_osiz:
            var_ayzf = var_wrnh + var_osiz >> 1
            if var_ayzf in var_rgwu:
                var_wnki = var_rgwu[var_ayzf]
            else:
                var_wnki = arg_rcsn.get(var_ayzf)
                var_rgwu[var_ayzf] = var_wnki
            if var_ayzf + 1 in var_rgwu:
                var_egyk = var_rgwu[var_ayzf + 1]
            else:
                var_egyk = arg_rcsn.get(var_ayzf + 1)
                var_rgwu[var_ayzf + 1] = var_egyk
            if var_wnki < var_egyk:
                if var_wnki == arg_xdvx:
                    return var_ayzf
                if var_egyk == arg_xdvx:
                    return var_ayzf + 1
                var_wrnh = var_ayzf + 1
            else:
                var_osiz = var_ayzf
        var_dcmd = var_wrnh
        var_wrnh = 0
        var_osiz = var_dcmd
        while var_wrnh <= var_osiz:
            var_ayzf = var_wrnh + var_osiz >> 1
            if var_ayzf in var_rgwu:
                var_wnki = var_rgwu[var_ayzf]
            else:
                var_wnki = arg_rcsn.get(var_ayzf)
            if var_wnki == arg_xdvx:
                return var_ayzf
            elif var_wnki < arg_xdvx:
                var_wrnh = var_ayzf + 1
            else:
                var_osiz = var_ayzf - 1
        var_wrnh = var_dcmd + 1
        var_osiz = var_hqta - 1
        while var_wrnh <= var_osiz:
            var_ayzf = var_wrnh + var_osiz >> 1
            if var_ayzf in var_rgwu:
                var_wnki = var_rgwu[var_ayzf]
            else:
                var_wnki = arg_rcsn.get(var_ayzf)
            if var_wnki == arg_xdvx:
                return var_ayzf
            elif var_wnki > arg_xdvx:
                var_wrnh = var_ayzf + 1
            else:
                var_osiz = var_ayzf - 1
        return -1
