class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 10 ** 9 + 7
        var_rgwu = {}
        var_wrnh = {}
        for var_osiz in arg_xdvx:
            var_rgwu[var_osiz] = var_rgwu.get(var_osiz, 0) + 1
        var_ayzf = 0
        for var_osiz in arg_xdvx:
            var_wnki = var_osiz * 2
            var_egyk = var_wrnh.get(var_wnki, 0)
            var_wrnh[var_osiz] = var_wrnh.get(var_osiz, 0) + 1
            var_dcmd = var_rgwu.get(var_wnki, 0) - var_wrnh.get(var_wnki, 0)
            var_ayzf = (var_ayzf + var_egyk * var_dcmd) % var_hqta
        return var_ayzf
