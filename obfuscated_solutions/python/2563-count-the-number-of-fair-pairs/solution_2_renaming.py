class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        arg_xdvx.sort()
        return arg_ihhe.lower_bound(arg_xdvx, arg_bacg + 1
            ) - arg_ihhe.lower_bound(arg_xdvx, arg_rcsn)

    def func_wrnh(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_osiz: var_rgwu
        ) ->var_rgwu:
        var_ayzf = 0
        var_wnki = var_egyk(arg_xdvx) - 1
        var_dcmd = 0
        while var_ayzf < var_wnki:
            var_llti = arg_xdvx[var_ayzf] + arg_xdvx[var_wnki]
            if var_llti < arg_osiz:
                var_dcmd += var_wnki - var_ayzf
                var_ayzf += 1
            else:
                var_wnki -= 1
        return var_dcmd
