from sortedcontainers import SortedList


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = [1] * var_rgwu(arg_xdvx)
        var_wrnh = var_osiz()
        var_ayzf = {}
        for var_wnki, var_egyk in var_dcmd(arg_xdvx):
            if var_egyk == 0:
                var_wrnh.add(var_wnki)
            else:
                var_hqta[var_wnki] = -1
                if var_egyk in var_ayzf:
                    var_llti = var_wrnh.bisect(var_ayzf[var_egyk])
                    if var_llti == var_rgwu(var_wrnh):
                        return []
                    var_hqta[var_wrnh[var_llti]] = var_egyk
                    var_wrnh.discard(var_wrnh[var_llti])
                var_ayzf[var_egyk] = var_wnki
        return var_hqta
