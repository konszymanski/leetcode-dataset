class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_osiz:
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            var_rgwu += arg_ihhe._has_prefix(var_wrnh, arg_rcsn)
        return var_rgwu

    def func_ayzf(arg_ihhe, var_hqta: var_hqta, arg_rcsn: var_hqta) ->var_osiz:
        var_wnki = 0
        while var_wnki < var_egyk(var_hqta) and var_wnki < var_egyk(arg_rcsn):
            if var_hqta[var_wnki] != arg_rcsn[var_wnki]:
                return 0
            var_wnki += 1
        if var_wnki != var_egyk(arg_rcsn):
            return 0
        return 1
