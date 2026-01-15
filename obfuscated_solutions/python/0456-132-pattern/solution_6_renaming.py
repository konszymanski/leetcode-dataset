class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_dcmd:
        if var_hqta(arg_xdvx) < 3:
            return False
        var_rgwu = [-1] * var_hqta(arg_xdvx)
        var_rgwu[0] = arg_xdvx[0]
        for var_wrnh in var_osiz(1, var_hqta(arg_xdvx)):
            var_rgwu[var_wrnh] = var_ayzf(var_rgwu[var_wrnh - 1], arg_xdvx[
                var_wrnh])
        var_wnki = var_hqta(arg_xdvx)
        for var_egyk in var_osiz(var_hqta(arg_xdvx) - 1, -1, -1):
            if arg_xdvx[var_egyk] <= var_rgwu[var_egyk]:
                continue
            while var_wnki < var_hqta(arg_xdvx) and arg_xdvx[var_wnki
                ] <= var_rgwu[var_egyk]:
                var_wnki += 1
            if var_wnki < var_hqta(arg_xdvx) and arg_xdvx[var_wnki] < arg_xdvx[
                var_egyk]:
                return True
            var_wnki -= 1
            arg_xdvx[var_wnki] = arg_xdvx[var_egyk]
        return False
