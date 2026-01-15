class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:

        @var_llti
        def func_hqta(arg_rgwu, arg_wrnh):
            if arg_wrnh == var_osiz:
                return 1
            if arg_rgwu > 40:
                return 0
            var_ayzf = func_hqta(arg_rgwu + 1, arg_wrnh)
            for var_wnki in var_egyk[arg_rgwu]:
                if arg_wrnh & 1 << var_wnki == 0:
                    var_ayzf = (var_ayzf + func_hqta(arg_rgwu + 1, arg_wrnh |
                        1 << var_wnki)) % var_dcmd
            return var_ayzf
        var_egyk = var_zbxo(var_rdmc)
        for var_rjut in var_lsgw(var_cbvh(arg_xdvx)):
            for arg_rgwu in arg_xdvx[var_rjut]:
                var_egyk[arg_rgwu].append(var_rjut)
        var_yjch = var_cbvh(arg_xdvx)
        var_dcmd = 10 ** 9 + 7
        var_osiz = 2 ** var_yjch - 1
        return func_hqta(1, 0)
