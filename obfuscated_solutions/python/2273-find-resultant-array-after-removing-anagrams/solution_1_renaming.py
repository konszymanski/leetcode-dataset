class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = [arg_xdvx[0]]
        var_rgwu = var_wrnh(arg_xdvx)

        def func_osiz(arg_ayzf: var_bacg, arg_wnki: var_bacg) ->var_rjut:
            var_egyk = [0] * 26
            for var_dcmd in arg_ayzf:
                var_egyk[var_llti(var_dcmd) - var_llti('a')] += 1
            for var_dcmd in arg_wnki:
                var_egyk[var_llti(var_dcmd) - var_llti('a')] -= 1
            return var_zbxo(var_rdmc == 0 for var_rdmc in var_egyk)
        for var_lsgw in var_cbvh(1, var_rgwu):
            if func_osiz(arg_xdvx[var_lsgw], arg_xdvx[var_lsgw - 1]):
                continue
            var_hqta.append(arg_xdvx[var_lsgw])
        return var_hqta
