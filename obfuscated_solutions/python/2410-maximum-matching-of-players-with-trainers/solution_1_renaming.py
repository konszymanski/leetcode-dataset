class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        arg_xdvx.sort()
        arg_rcsn.sort()
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_rcsn)
        var_ayzf = var_wnki = var_egyk = 0
        while var_ayzf < var_rgwu and var_wnki < var_wrnh:
            while var_wnki < var_wrnh and arg_xdvx[var_ayzf] > arg_rcsn[
                var_wnki]:
                var_wnki += 1
            if var_wnki < var_wrnh:
                var_egyk += 1
            var_ayzf += 1
            var_wnki += 1
        return var_egyk
