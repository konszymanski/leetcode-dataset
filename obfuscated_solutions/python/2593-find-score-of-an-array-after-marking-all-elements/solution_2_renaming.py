class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        var_bacg = [False] * var_hqta(arg_xdvx)
        var_rgwu = []
        for var_wrnh in var_osiz(var_hqta(arg_xdvx)):
            var_ayzf.heappush(var_rgwu, (arg_xdvx[var_wrnh], var_wrnh))
        while var_rgwu:
            var_wnki, var_egyk = var_ayzf.heappop(var_rgwu)
            if not var_bacg[var_egyk]:
                var_rcsn += var_wnki
                var_bacg[var_egyk] = True
                if var_egyk - 1 >= 0:
                    var_bacg[var_egyk - 1] = True
                if var_egyk + 1 < var_hqta(arg_xdvx):
                    var_bacg[var_egyk + 1] = True
        return var_rcsn
