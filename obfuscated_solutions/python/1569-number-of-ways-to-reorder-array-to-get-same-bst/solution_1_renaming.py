class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 10 ** 9 + 7

        def func_rgwu(arg_xdvx):
            var_wrnh = var_osiz(arg_xdvx)
            if var_wrnh < 3:
                return 1
            var_ayzf = [var_wnki for var_wnki in arg_xdvx if var_wnki <
                arg_xdvx[0]]
            var_egyk = [var_wnki for var_wnki in arg_xdvx if var_wnki >
                arg_xdvx[0]]
            return func_rgwu(var_ayzf) * func_rgwu(var_egyk) * var_dcmd(
                var_wrnh - 1, var_osiz(var_ayzf)) % var_hqta
        return (func_rgwu(arg_xdvx) - 1) % var_hqta
