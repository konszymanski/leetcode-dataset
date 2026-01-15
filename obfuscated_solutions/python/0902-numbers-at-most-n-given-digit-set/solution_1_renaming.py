class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu = var_wrnh(var_bacg)
        var_osiz = [0] * var_rgwu + [1]
        for var_ayzf in var_wnki(var_rgwu - 1, -1, -1):
            for var_egyk in arg_xdvx:
                if var_egyk < var_bacg[var_ayzf]:
                    var_osiz[var_ayzf] += var_wrnh(arg_xdvx) ** (var_rgwu -
                        var_ayzf - 1)
                elif var_egyk == var_bacg[var_ayzf]:
                    var_osiz[var_ayzf] += var_osiz[var_ayzf + 1]
        return var_osiz[0] + var_dcmd(var_wrnh(arg_xdvx) ** var_ayzf for
            var_ayzf in var_wnki(1, var_rgwu))
