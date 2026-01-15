class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_ayzf:
        var_rgwu = {}
        for var_wrnh in arg_rcsn:
            var_rgwu[var_wrnh] = var_rgwu.get(var_wrnh, 0) + 1
        for var_wrnh in arg_xdvx:
            if var_wrnh not in var_rgwu:
                return False
            var_rgwu[var_wrnh] -= 1
            if var_rgwu[var_wrnh] == 0:
                del var_rgwu[var_wrnh]
        return var_osiz(var_rgwu) == 0
