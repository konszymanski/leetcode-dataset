class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: 'MountainArray'
        ) ->var_bacg:
        var_hqta = arg_rcsn.length()
        var_rgwu = 1
        var_wrnh = var_hqta - 2
        while var_rgwu != var_wrnh:
            var_osiz = var_rgwu + var_wrnh >> 1
            var_ayzf = arg_rcsn.get(var_osiz)
            var_wnki = arg_rcsn.get(var_osiz + 1)
            if var_ayzf < var_wnki:
                if var_ayzf == arg_xdvx:
                    return var_osiz
                if var_wnki == arg_xdvx:
                    return var_osiz + 1
                var_rgwu = var_osiz + 1
            else:
                var_wrnh = var_osiz
        var_egyk = var_rgwu
        var_rgwu = 0
        var_wrnh = var_egyk
        while var_rgwu <= var_wrnh:
            var_osiz = var_rgwu + var_wrnh >> 1
            var_ayzf = arg_rcsn.get(var_osiz)
            if var_ayzf == arg_xdvx:
                return var_osiz
            elif var_ayzf < arg_xdvx:
                var_rgwu = var_osiz + 1
            else:
                var_wrnh = var_osiz - 1
        var_rgwu = var_egyk + 1
        var_wrnh = var_hqta - 1
        while var_rgwu <= var_wrnh:
            var_osiz = var_rgwu + var_wrnh >> 1
            var_ayzf = arg_rcsn.get(var_osiz)
            if var_ayzf == arg_xdvx:
                return var_osiz
            elif var_ayzf > arg_xdvx:
                var_rgwu = var_osiz + 1
            else:
                var_wrnh = var_osiz - 1
        return -1
