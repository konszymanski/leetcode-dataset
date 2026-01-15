class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_dcmd:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [([False] * (var_bacg + 1)) for var_wrnh in var_osiz(
            var_bacg + 1)]
        var_rgwu[var_bacg][0] = True
        for var_ayzf in var_osiz(var_bacg - 1, -1, -1):
            for var_wnki in var_osiz(var_bacg):
                var_egyk = False
                if arg_xdvx[var_ayzf] == '*':
                    if var_wnki < var_bacg:
                        var_egyk |= var_rgwu[var_ayzf + 1][var_wnki + 1]
                    if var_wnki > 0:
                        var_egyk |= var_rgwu[var_ayzf + 1][var_wnki - 1]
                    var_egyk |= var_rgwu[var_ayzf + 1][var_wnki]
                elif arg_xdvx[var_ayzf] == '(':
                    var_egyk |= var_rgwu[var_ayzf + 1][var_wnki + 1]
                elif var_wnki > 0:
                    var_egyk |= var_rgwu[var_ayzf + 1][var_wnki - 1]
                var_rgwu[var_ayzf][var_wnki] = var_egyk
        return var_rgwu[0][0]
