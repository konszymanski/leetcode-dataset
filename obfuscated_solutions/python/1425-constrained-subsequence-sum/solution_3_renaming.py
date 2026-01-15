class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh()
        var_osiz = [0] * var_ayzf(arg_xdvx)
        for var_wnki in var_egyk(var_ayzf(arg_xdvx)):
            if var_rgwu and var_wnki - var_rgwu[0] > arg_rcsn:
                var_rgwu.popleft()
            var_osiz[var_wnki] = (var_osiz[var_rgwu[0]] if var_rgwu else 0
                ) + arg_xdvx[var_wnki]
            while var_rgwu and var_osiz[var_rgwu[-1]] < var_osiz[var_wnki]:
                var_rgwu.pop()
            if var_osiz[var_wnki] > 0:
                var_rgwu.append(var_wnki)
        return var_dcmd(var_osiz)
