class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = -1
        var_rgwu = var_wrnh()
        for var_osiz in arg_xdvx:
            var_ayzf = var_wnki(var_osiz)
            if var_ayzf > var_hqta and -var_osiz + 1024 in var_rgwu:
                var_hqta = var_ayzf
            var_rgwu.add(var_osiz + 1024)
        return var_hqta
