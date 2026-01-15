class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 10 ** 9 + 7
        var_rgwu = [0] * (arg_xdvx + 1)
        var_rgwu[0] = 1
        for var_wrnh in var_osiz(1, arg_xdvx + 1):
            var_ayzf = var_wrnh ** arg_rcsn
            if var_ayzf > arg_xdvx:
                break
            for var_wnki in var_osiz(arg_xdvx, var_ayzf - 1, -1):
                var_rgwu[var_wnki] = (var_rgwu[var_wnki] + var_rgwu[
                    var_wnki - var_ayzf]) % var_hqta
        return var_rgwu[arg_xdvx]
