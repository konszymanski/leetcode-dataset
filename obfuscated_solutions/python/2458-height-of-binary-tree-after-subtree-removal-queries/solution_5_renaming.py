class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_rgwu[var_wrnh]) ->var_rgwu[var_wrnh]:
        var_osiz = {}
        var_ayzf = {}
        var_wnki = {}
        var_egyk = {}

        def func_dcmd(arg_llti, arg_zbxo):
            if not arg_llti:
                return 0
            var_osiz[arg_llti.val] = arg_zbxo
            var_rdmc = func_dcmd(arg_llti.left, arg_zbxo + 1)
            var_rjut = func_dcmd(arg_llti.right, arg_zbxo + 1)
            var_lsgw = 1 + var_cbvh(var_rdmc, var_rjut)
            var_ayzf[arg_llti.val] = var_lsgw
            if var_lsgw > var_wnki.get(arg_zbxo, 0):
                var_egyk[arg_zbxo] = var_wnki.get(arg_zbxo, 0)
                var_wnki[arg_zbxo] = var_lsgw
            elif var_lsgw > var_egyk.get(arg_zbxo, 0):
                var_egyk[arg_zbxo] = var_lsgw
            return var_lsgw
        func_dcmd(arg_xdvx, 0)
        return [(var_osiz[var_yjch] + (var_egyk.get(var_osiz[var_yjch], 0) if
            var_ayzf[var_yjch] == var_wnki[var_osiz[var_yjch]] else
            var_wnki.get(var_osiz[var_yjch], 0)) - 1) for var_yjch in arg_rcsn]
