class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_dcmd:
        var_hqta = var_rgwu(arg_xdvx)
        for var_wrnh in var_osiz(var_hqta):
            var_ayzf = []
            for var_wnki in var_osiz(var_wrnh, var_hqta):
                var_ayzf.append(arg_xdvx[var_wnki])
            for var_wnki in var_osiz(var_wrnh):
                var_ayzf.append(arg_xdvx[var_wnki])
            var_egyk = True
            for var_wnki in var_osiz(var_hqta - 1):
                if var_ayzf[var_wnki] > var_ayzf[var_wnki + 1]:
                    var_egyk = False
                    break
            if var_egyk:
                return True
        return False
