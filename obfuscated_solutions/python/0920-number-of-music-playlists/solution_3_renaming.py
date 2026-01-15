class Solution:
    var_udax = 1000000007

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = 1
        while arg_bacg > 0:
            if arg_bacg & 1:
                var_hqta = var_hqta * arg_rcsn % arg_xdvx.MOD
            arg_bacg >>= 1
            arg_rcsn = arg_rcsn * arg_rcsn % arg_xdvx.MOD
        return var_hqta

    def func_rgwu(arg_xdvx, arg_wrnh):
        arg_xdvx.factorial = [1] * (arg_wrnh + 1)
        arg_xdvx.inv_factorial = [1] * (arg_wrnh + 1)
        for var_osiz in var_ayzf(1, arg_wrnh + 1):
            arg_xdvx.factorial[var_osiz] = arg_xdvx.factorial[var_osiz - 1
                ] * var_osiz % arg_xdvx.MOD
            arg_xdvx.inv_factorial[var_osiz] = arg_xdvx.power(arg_xdvx.
                factorial[var_osiz], arg_xdvx.MOD - 2)

    def func_wnki(arg_xdvx, arg_wrnh, arg_egyk, arg_dcmd):
        arg_xdvx.precalculate_factorials(arg_wrnh)
        var_llti = 1
        var_zbxo = 0
        for var_osiz in var_ayzf(arg_wrnh, arg_dcmd - 1, -1):
            var_rdmc = arg_xdvx.power(var_osiz - arg_dcmd, arg_egyk - arg_dcmd)
            var_rdmc = var_rdmc * arg_xdvx.inv_factorial[arg_wrnh - var_osiz
                ] % arg_xdvx.MOD
            var_rdmc = var_rdmc * arg_xdvx.inv_factorial[var_osiz - arg_dcmd
                ] % arg_xdvx.MOD
            var_zbxo = (var_zbxo + var_llti * var_rdmc + arg_xdvx.MOD
                ) % arg_xdvx.MOD
            var_llti *= -1
        return arg_xdvx.factorial[arg_wrnh] * var_zbxo % arg_xdvx.MOD
