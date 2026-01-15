class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_llti:
        var_rgwu = []
        var_wrnh = []
        for var_osiz in arg_xdvx:
            for var_ayzf in var_osiz:
                var_rgwu.append(var_ayzf)
        for var_osiz in arg_rcsn:
            for var_ayzf in var_osiz:
                var_wrnh.append(var_ayzf)
        if var_wnki(var_rgwu) != var_wnki(var_wrnh):
            return False
        for var_egyk in var_dcmd(var_wnki(var_rgwu)):
            if var_rgwu[var_egyk] != var_wrnh[var_egyk]:
                return False
        return True
