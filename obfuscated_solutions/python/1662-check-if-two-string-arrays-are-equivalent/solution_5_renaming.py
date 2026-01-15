class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_egyk:
        var_rgwu = ''.join(arg_rcsn)
        var_wrnh = 0
        for var_osiz in arg_xdvx:
            for var_ayzf in var_osiz:
                if var_wrnh >= var_wnki(var_rgwu) or var_ayzf != var_rgwu[
                    var_wrnh]:
                    return False
                var_wrnh += 1
        return var_wrnh == var_wnki(var_rgwu)
