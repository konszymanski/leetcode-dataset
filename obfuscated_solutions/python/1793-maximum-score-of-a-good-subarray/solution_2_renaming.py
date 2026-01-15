class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [-1] * var_rgwu
        var_ayzf = []
        for var_wnki in var_egyk(var_rgwu - 1, -1, -1):
            while var_ayzf and arg_xdvx[var_ayzf[-1]] > arg_xdvx[var_wnki]:
                var_osiz[var_ayzf.pop()] = var_wnki
            var_ayzf.append(var_wnki)
        var_dcmd = [var_rgwu] * var_rgwu
        var_ayzf = []
        for var_wnki in var_egyk(var_rgwu):
            while var_ayzf and arg_xdvx[var_ayzf[-1]] > arg_xdvx[var_wnki]:
                var_dcmd[var_ayzf.pop()] = var_wnki
            var_ayzf.append(var_wnki)
        var_llti = 0
        for var_wnki in var_egyk(var_rgwu):
            if var_osiz[var_wnki] < arg_rcsn and var_dcmd[var_wnki] > arg_rcsn:
                var_llti = var_zbxo(var_llti, arg_xdvx[var_wnki] * (
                    var_dcmd[var_wnki] - var_osiz[var_wnki] - 1))
        return var_llti
