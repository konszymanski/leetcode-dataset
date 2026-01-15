class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_egyk:
        var_rgwu = []
        for var_wrnh in arg_rcsn:
            var_rgwu.extend(var_wrnh)
        var_osiz = 0
        for var_wrnh in arg_xdvx:
            for var_ayzf in var_wrnh:
                if var_osiz >= var_wnki(var_rgwu) or var_ayzf != var_rgwu[
                    var_osiz]:
                    return False
                var_osiz += 1
        return var_osiz == var_wnki(var_rgwu)
