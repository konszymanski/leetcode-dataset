class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_bacg)
        var_wrnh = [[] for var_osiz in var_ayzf(var_hqta)]
        var_wnki = [0] * var_hqta
        for var_egyk in arg_xdvx:
            var_wrnh[var_egyk[0]].append(var_egyk[1])
            var_wrnh[var_egyk[1]].append(var_egyk[0])

        def func_dcmd(arg_llti, arg_zbxo, arg_rdmc):
            var_rjut = 0
            var_lsgw = var_cbvh('-inf')
            if arg_llti == arg_rcsn:
                var_wnki[arg_llti] = 0
            else:
                var_wnki[arg_llti] = var_hqta
            for var_yjch in var_wrnh[arg_llti]:
                if var_yjch != arg_zbxo:
                    var_lsgw = var_dmio(var_lsgw, func_dcmd(var_yjch,
                        arg_llti, arg_rdmc + 1))
                    var_wnki[arg_llti] = var_ulfl(var_wnki[arg_llti], 
                        var_wnki[var_yjch] + 1)
            if var_wnki[arg_llti] > arg_rdmc:
                var_rjut += arg_bacg[arg_llti]
            elif var_wnki[arg_llti] == arg_rdmc:
                var_rjut += arg_bacg[arg_llti] // 2
            return var_rjut if var_lsgw == var_cbvh('-inf'
                ) else var_rjut + var_lsgw
        return func_dcmd(0, -1, 0)
