class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_hqta[var_bacg]:
        var_rgwu = 10 ** 9 + 7
        var_wrnh, var_osiz = [], 1
        while arg_xdvx > 0:
            if arg_xdvx % 2 == 1:
                var_wrnh.append(var_osiz)
            arg_xdvx //= 2
            var_osiz *= 2
        var_ayzf = []
        for var_wnki, var_egyk in arg_rcsn:
            var_dcmd = 1
            for var_llti in var_zbxo(var_wnki, var_egyk + 1):
                var_dcmd = var_dcmd * var_wrnh[var_llti] % var_rgwu
            var_ayzf.append(var_dcmd)
        return var_ayzf
