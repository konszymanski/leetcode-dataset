class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_rcsn[var_bacg]]:
        var_hqta = var_rgwu(arg_xdvx)
        for var_wrnh in var_osiz(var_hqta):
            var_ayzf = [arg_xdvx[var_wrnh + var_wnki][var_wnki] for
                var_wnki in var_osiz(var_hqta - var_wrnh)]
            var_ayzf.sort(reverse=True)
            for var_wnki in var_osiz(var_hqta - var_wrnh):
                arg_xdvx[var_wrnh + var_wnki][var_wnki] = var_ayzf[var_wnki]
        for var_wnki in var_osiz(1, var_hqta):
            var_ayzf = [arg_xdvx[var_wrnh][var_wnki + var_wrnh] for
                var_wrnh in var_osiz(var_hqta - var_wnki)]
            var_ayzf.sort()
            for var_wrnh in var_osiz(var_hqta - var_wnki):
                arg_xdvx[var_wrnh][var_wnki + var_wrnh] = var_ayzf[var_wrnh]
        return arg_xdvx
