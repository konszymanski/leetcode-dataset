class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [0] * var_hqta
        var_osiz, var_ayzf = 0, 1
        for var_wnki in var_egyk(var_hqta):
            if arg_xdvx[var_wnki] > 0:
                var_wrnh[var_osiz] = arg_xdvx[var_wnki]
                var_osiz += 2
            else:
                var_wrnh[var_ayzf] = arg_xdvx[var_wnki]
                var_ayzf += 2
        return var_wrnh
