class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx) - 1):
            var_ayzf = 0
            for var_wnki in var_wrnh(var_rgwu + 1, var_osiz(arg_xdvx)):
                var_ayzf ^= arg_xdvx[var_wnki - 1]
                var_egyk = 0
                for var_dcmd in var_wrnh(var_wnki, var_osiz(arg_xdvx)):
                    var_egyk ^= arg_xdvx[var_dcmd]
                    if var_ayzf == var_egyk:
                        var_hqta += 1
        return var_hqta
