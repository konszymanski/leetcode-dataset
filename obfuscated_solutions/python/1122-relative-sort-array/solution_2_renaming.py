class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = {}
        var_wrnh = []
        var_osiz = []
        for var_ayzf in arg_rcsn:
            var_rgwu[var_ayzf] = 0
        for var_ayzf in arg_xdvx:
            if var_ayzf in var_rgwu:
                var_rgwu[var_ayzf] += 1
            else:
                var_wrnh.append(var_ayzf)
        var_wrnh.sort()
        for var_ayzf in arg_rcsn:
            for var_wnki in var_egyk(var_rgwu[var_ayzf]):
                var_osiz.append(var_ayzf)
        var_osiz.extend(var_wrnh)
        return var_osiz
