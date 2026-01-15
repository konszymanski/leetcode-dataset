class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_egyk:
        var_rgwu = {}
        for var_wrnh in arg_rcsn:
            if var_wrnh not in var_rgwu:
                var_rgwu[var_wrnh] = 1
            else:
                var_rgwu[var_wrnh] += 1
        var_osiz = {}
        for var_wrnh in arg_xdvx:
            if var_wrnh not in var_osiz:
                var_osiz[var_wrnh] = 1
            else:
                var_osiz[var_wrnh] += 1
        if var_ayzf(var_rgwu) != var_ayzf(var_osiz):
            return False
        for var_wnki in var_rgwu:
            if var_rgwu[var_wnki] != var_osiz.get(var_wnki, 0):
                return False
        return True
