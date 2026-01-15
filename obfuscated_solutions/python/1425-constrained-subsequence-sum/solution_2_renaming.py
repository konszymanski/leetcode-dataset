from sortedcontainers import SortedList


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh([0])
        var_osiz = [0] * var_ayzf(arg_xdvx)
        for var_wnki in var_egyk(var_ayzf(arg_xdvx)):
            var_osiz[var_wnki] = arg_xdvx[var_wnki] + var_rgwu[-1]
            var_rgwu.add(var_osiz[var_wnki])
            if var_wnki >= arg_rcsn:
                var_rgwu.remove(var_osiz[var_wnki - arg_rcsn])
        return var_dcmd(var_osiz)
