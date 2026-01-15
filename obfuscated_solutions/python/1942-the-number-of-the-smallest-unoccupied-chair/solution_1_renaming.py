class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = arg_xdvx[arg_rcsn]
        arg_xdvx.sort()
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [0] * var_wrnh
        for var_wnki in arg_xdvx:
            for var_egyk in var_dcmd(var_wrnh):
                if var_ayzf[var_egyk] <= var_wnki[0]:
                    var_ayzf[var_egyk] = var_wnki[1]
                    if var_wnki == var_rgwu:
                        return var_egyk
                    break
        return 0
