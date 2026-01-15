class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_ayzf[
        var_bacg]:
        from collections import defaultdict
        var_hqta = var_rgwu(var_wrnh)
        for var_osiz in arg_xdvx.split():
            var_hqta[var_osiz] += 1
        for var_osiz in arg_rcsn.split():
            var_hqta[var_osiz] += 1
        return [var_osiz for var_osiz in var_hqta if var_hqta[var_osiz] == 1]
