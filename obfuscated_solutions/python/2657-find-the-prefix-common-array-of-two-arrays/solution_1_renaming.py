class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [0] * var_hqta
        for var_osiz in var_ayzf(var_hqta):
            var_wnki = 0
            for var_egyk in var_ayzf(var_osiz + 1):
                for var_dcmd in var_ayzf(var_osiz + 1):
                    if arg_xdvx[var_egyk] == arg_rcsn[var_dcmd]:
                        var_wnki += 1
                        break
            var_wrnh[var_osiz] = var_wnki
        return var_wrnh
