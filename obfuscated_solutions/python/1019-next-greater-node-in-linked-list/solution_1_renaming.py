class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk[var_dcmd]:
        values = []
        while arg_xdvx:
            values.append(arg_xdvx.val)
            arg_xdvx = arg_xdvx.next
        var_bacg = [0] * var_hqta(values)
        var_rgwu = []
        for var_wrnh, var_osiz in var_ayzf(values):
            while var_rgwu and values[var_rgwu[-1]] < var_osiz:
                var_wnki = var_rgwu.pop()
                var_bacg[var_wnki] = var_osiz
            var_rgwu.append(var_wrnh)
        return var_bacg
